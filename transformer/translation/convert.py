from datasets import load_dataset
from transformers import MarianTokenizer

# 1. 加载 parquet 文件
dataset = load_dataset('parquet', data_files={'train': 'train-00000-of-00013.parquet', 'validation': 'validation-00000-of-00001.parquet'})

# 2. 解析 'translation' 列
def parse_translation_column(example):
    translations = example['translation']
    # 假设 'translation' 列包含一个字典，格式为 {'en': '...', 'zh': '...'}
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
tokenized_datasets = dataset.map(preprocess_function, batched=True)

# 查看数据集结构以确保正确解析
print(tokenized_datasets['train'].column_names)
