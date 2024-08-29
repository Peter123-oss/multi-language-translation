import requests
import json

API_KEY = "juJfp7qPISmmqgWRiXxqoPCh"
SECRET_KEY = "8Dr2QYeSkA789CyHNEMTM3ssk29EmBnS"


def main():
    url = "https://vop.baidu.com/pro_api"

    payload = json.dumps({
        "format": "pcm",
        "rate": 16000,
        "channel": 1,
        "cuid": "WvleesC18mZg83ls7y6CoGi0xsicMjrz",
        "token": get_access_token(),
        "dev_pid": 80001
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


if __name__ == '__main__':
    main()
