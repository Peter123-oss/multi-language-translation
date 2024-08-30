from transformers import MarianMTModel, MarianTokenizer

# 加载微调后的模型和分词器
model = MarianMTModel.from_pretrained('./fine_tuned_marianmt')
tokenizer = MarianTokenizer.from_pretrained('./fine_tuned_marianmt')

# 进行翻译
src_text = ["美国国家安全顾问沙利文（Jake Sullivan）周二（8月27日）抵达北京，展开为期三天的访华行程，这是沙利文首次访问中国，也是自2016年以来首位访华的美国国家安全顾问。在中美两国努力稳定关系之际，沙利文抵京与中国外长王毅举行了会谈。过去16个月，沙利文和王毅已经有过四次会晤，地点分别在维也纳、马耳他、华盛顿和曼谷。他们最近一次会面是在今年一月，适逢是中国国家主席习近平和美国总统拜登总统举行了一次重要的会面之后，试图重新调整两国之间的关系。本周的会谈显示出中国以及习近平仍然是拜登政府其中一个优先的方向，即使拜登的任期只剩下最后几个月。无论是沙利文还是王毅，两人都承认有必要在两国的分歧之中找到共同点。"]
encoded_input = tokenizer(src_text, return_tensors="pt", padding=True, truncation=True)
translated_tokens = model.generate(**encoded_input)
translated_text = [tokenizer.decode(t, skip_special_tokens=True) for t in translated_tokens]

print(translated_text)