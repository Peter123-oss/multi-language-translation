from transformers import MarianMTModel, MarianTokenizer

# 指定模型名称
model_name = "Helsinki-NLP/opus-mt-zh-en"

# 加载分词器和模型
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# 输入中文文本
src_text = ["床前明月光，疑是地上霜"]

# 使用分词器进行编码
encoded_input = tokenizer(src_text, return_tensors="pt", padding=True, truncation=True)

# 生成翻译
translated_tokens = model.generate(**encoded_input)

# 解码生成的翻译，显式设置 clean_up_tokenization_spaces 为 True
translated_text = [
    tokenizer.decode(t, skip_special_tokens=True, clean_up_tokenization_spaces=True)
    for t in translated_tokens
]

print(translated_text)  # 输出: ['This is a test sentence.']
