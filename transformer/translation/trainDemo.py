import os
import shutil
from datasets import load_dataset
from transformers import MarianTokenizer, MarianMTModel, Seq2SeqTrainingArguments, Seq2SeqTrainer
import torch

def main():
    # 清理缓存目录，确保不存在冲突的缓存文件
    cache_dir = os.path.expanduser("~/.cache/huggingface/datasets/")
    if os.path.exists(cache_dir):
        shutil.rmtree(cache_dir)

    # 1. 加载 parquet 文件
    dataset = load_dataset('parquet', data_files={'train': 'train-00000-of-00013.parquet', 'validation': 'validation-00000-of-00001.parquet'})

    # 选择训练集的前4000行数据
    dataset['train'] = dataset['train'].select(range(4000))

    # 2. 解析 'translation' 列
    def parse_translation_column(example):
        translations = example['translation']
        return {'src': translations['zh'], 'tgt': translations['en']}

    # 应用解析函数
    dataset = dataset.map(parse_translation_column)

    # 3. 加载分词器
    model_name = "Helsinki-NLP/opus-mt-zh-en"
    tokenizer = MarianTokenizer.from_pretrained(model_name)

    # 4. 定义预处理函数
    def preprocess_function(examples):
        inputs = tokenizer(examples['src'], truncation=True, padding='max_length', max_length=128)
        targets = tokenizer(examples['tgt'], truncation=True, padding='max_length', max_length=128)
        inputs['labels'] = targets['input_ids']
        return inputs

    # 5. 预处理数据集
    tokenized_datasets = dataset.map(preprocess_function, batched=True, num_proc=4)  # 使用多进程加速

    # 6. 加载预训练模型并移动到GPU
    model = MarianMTModel.from_pretrained(model_name)
    if torch.cuda.is_available():
        model.to('cuda')

    # 7. 设置训练参数
    training_args = Seq2SeqTrainingArguments(
        output_dir='./results',
        evaluation_strategy='epoch',
        learning_rate=2e-5,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=16,
        weight_decay=0.01,
        save_total_limit=3,
        num_train_epochs=3,
        predict_with_generate=True,
        fp16=True  # 启用混合精度训练，进一步加速
    )

    # 8. 创建Trainer
    trainer = Seq2SeqTrainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_datasets['train'],
        eval_dataset=tokenized_datasets['validation'],
        tokenizer=tokenizer
    )

    # 9. 开始训练
    trainer.train()

    # 10. 评估模型
    eval_results = trainer.evaluate()
    print(eval_results)

    # 11. 保存微调后的模型
    trainer.save_model("./fine_tuned_marianmt")
    tokenizer.save_pretrained("./fine_tuned_marianmt")

if __name__ == '__main__':
    main()
