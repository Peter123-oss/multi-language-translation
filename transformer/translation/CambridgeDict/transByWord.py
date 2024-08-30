import http.client
import json

# 全局设置
BASE_URL = "dictionary.cambridge.org"
ACCESS_KEY = "HEOkZK6Y6onxbPDmo5WR6U2aVeSKPMbGD9kfA0igEdJegKAz13U5hrrzDaXcZCvi"  # 替换为你的实际API密钥


# 公用函数：发送GET请求
def send_get_request(endpoint, params=None):
    conn = http.client.HTTPSConnection(BASE_URL)

    headers = {
        "Accept": "application/json",
        "accessKey": ACCESS_KEY
    }

    # 构建带参数的URL
    url = f"{endpoint}"
    if params:
        url += "?" + "&".join([f"{key}={value}" for key, value in params.items()])

    # 发送请求
    conn.request("GET", url, headers=headers)

    # 获取响应
    res = conn.getresponse()
    data = res.read()

    # 关闭连接
    conn.close()

    # 返回解析后的JSON数据
    return json.loads(data.decode("utf-8"))


# 1. 获取字典列表
def get_dictionaries():
    return send_get_request("/api/v1/dictionaries")


# 2. 获取特定字典的信息
def get_dictionary(dict_code):
    return send_get_request(f"/api/v1/dictionaries/{dict_code}")


# 3. 获取字典条目 (API v1 未实现)
def get_entries(dict_code):
    return send_get_request(f"/api/v1/dictionaries/{dict_code}/entries")


# 4. 获取特定条目的完整信息
def get_entry(dict_code, entry_id, format="json"):
    params = {"format": format}
    return send_get_request(f"/api/v1/dictionaries/{dict_code}/entries/{entry_id}", params)


# 5. 查找特定条目周围的条目
def get_nearby_entries(dict_code, entry_id, entry_number=10):
    params = {"entrynumber": entry_number}
    return send_get_request(f"/api/v1/dictionaries/{dict_code}/entries/{entry_id}/nearbyentries", params)


# 6. 获取条目的发音
def get_entry_pronunciations(dict_code, entry_id, format="mp3", lang=None):
    params = {"format": format}
    if lang:
        params["lang"] = lang
    return send_get_request(f"/api/v1/dictionaries/{dict_code}/entries/{entry_id}/pronunciations", params)


# 7. 获取相关条目
def get_related_entries(dict_code, entry_id):
    return send_get_request(f"/api/v1/dictionaries/{dict_code}/entries/{entry_id}/relatedentries")


# 8. 在特定字典中搜索单词或短语
def search(dict_code, query, page_index=1, page_size=10):
    params = {"q": query, "pageindex": page_index, "pagesize": page_size}
    return send_get_request(f"/api/v1/dictionaries/{dict_code}/search", params)


# 9. 返回单词的拼写建议
def did_you_mean(dict_code, query, entry_number=10):
    params = {"q": query, "entrynumber": entry_number}
    return send_get_request(f"/api/v1/dictionaries/{dict_code}/search/didyoumean", params)


# 10. 搜索特定字典中的单词或短语，返回第一个结果的条目
def search_first(dict_code, query, format="json"):
    params = {"q": query, "format": format}
    return send_get_request(f"/api/v1/dictionaries/{dict_code}/search/first", params)


# 11. 获取字典的主题列表
def get_topics(dict_code):
    return send_get_request(f"/api/v1/dictionaries/{dict_code}/topics")


# 12. 获取特定词典主题的信息
def get_thesaurus(dict_code, thesaurus_name):
    return send_get_request(f"/api/v1/dictionaries/{dict_code}/topics/{thesaurus_name}")


# 13. 获取特定词典主题的信息
def get_topic(dict_code, thesaurus_name, topic_id):
    return send_get_request(f"/api/v1/dictionaries/{dict_code}/topics/{thesaurus_name}/{topic_id}")


# 14. 获取特定字典数据集的每日单词
def get_dictionary_word_of_the_day(dict_code, day=None, format="json"):
    params = {"day": day, "format": format} if day else {"format": format}
    return send_get_request(f"/api/v1/dictionaries/{dict_code}/wordoftheday", params)


# 15. 获取特定字典数据集的每日单词预览
def get_dictionary_word_of_the_day_preview(dict_code, day=None):
    params = {"day": day} if day else {}
    return send_get_request(f"/api/v1/dictionaries/{dict_code}/wordoftheday/preview", params)


# 16. 获取网站的每日单词
def get_word_of_the_day(day=None, format="json"):
    params = {"day": day, "format": format} if day else {"format": format}
    return send_get_request("/api/v1/wordoftheday", params)


# 17. 获取网站的每日单词预览
def get_word_of_the_day_preview(day=None):
    params = {"day": day} if day else {}
    return send_get_request("/api/v1/wordoftheday/preview", params)


# 示例使用
dictionaries = get_dictionaries()
print(dictionaries)

dictionary_info = get_dictionary("english-chinese-traditional")
print(dictionary_info)

search_results = search("english-chinese-traditional", "hello")
print(search_results)
