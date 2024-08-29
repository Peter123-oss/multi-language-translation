import base64
import json
import urllib

import requests
from PyPDF2 import PdfReader
from flask import jsonify

API_KEY = "az817g5nHqvu3pswviokqeCk"
SECRET_KEY = "miN4RrIB8TeLRIGhwmmtLt44NpbtUxcF"


# def main():
#     url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?access_token=" + get_access_token()
#     pdf_base64=get_file_content_as_base64("C:/Users/KUN/lfasr_new_python_demo/Our Journey to Spoken English.pdf", True)
#     pdf_file="pdf_file="+pdf_base64
#     payload = "pdf_file="+pdf_base64
#     headers = {
#         'Content-Type': 'application/x-www-form-urlencoded',
#         'Accept': 'application/json'
#     }
#
#     response = requests.request("POST", url, headers=headers, data=payload)
#     text=extract_text(response.json())
#
#     print(text)
def uploadFile1(path):
    """
    上传文件并返回其 base64 编码
    :param path: 文件路径
    :return: 字典，包含上传结果
    """
    pdf_text = get_file_content_as_base64(path, True)
    if not pdf_text:
        return {
            "code": -1,
            "message": "上传失败",
            "data": ""
        }
    return {
        "code": 0,
        "message": "上传成功",
        "data": pdf_text
    }

def convertToText(pdf_base64,page_count):
    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?access_token=" + get_access_token()

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }

    full_text = ""
    for i in range(page_count):
        payload = "pdf_file=" + pdf_base64 + f"&pdf_file_num={i + 1}"
        # 你可以在这里更新 payload 或者 URL 参数来处理每一页
        response = requests.post(url, headers=headers, data=payload)
        if response.status_code == 200:
            text = extract_text(response.json())
            full_text += text  # 将每页的文本追加到 full_text 中
        else:
            return {
                "code": -1,
                "message": f"转换失败：Error processing page {i + 1}: {response.status_code}, {response.text}",
                "data": full_text
            }
            # print(f"Error processing page {i + 1}: {response.status_code}, {response.text}")

    # print(full_text)  # 输出所有页面的文本

    return {
        "code": 0,
        "message": "转换成功",
        "data": full_text
    }


def get_file_content_as_base64(path, urlencoded=False):
    """
    获取文件base64编码
    :param path: 文件路径
    :param urlencoded: 是否对结果进行urlencoded
    :return: base64编码信息
    """
    with open(path, "rb") as f:
        content = base64.b64encode(f.read()).decode("utf8")
        if urlencoded:
            content = urllib.parse.quote_plus(content)
    return content


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))

def get_pdf_page_count(pdf_path):
    """
    获取PDF文件页数
    :param pdf_path: PDF文件路径
    :return: PDF文件的页数
    """
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        page_count = len(reader.pages)
    return page_count

def extract_text(data):
    # 提取 words_result 列表
    words_list = data.get("words_result", [])

    # 使用列表推导式提取所有 words 字段的值，并连接成一段话
    combined_words = ''.join([item["words"] for item in words_list])
    return combined_words



# if __name__ == '__main__':
#     main()