import requests
import ocr_idcard_sign
import base64


def get_content(plus_item):
    # 功能 API地址
    url = "https://api.ai.qq.com/fcgi-bin/ocr/ocr_idcardocr"
    # 获取请求参数
    payload = ocr_idcard_sign.get_params(plus_item)

    r = requests.post(url, data=payload)
    return r.json()


if __name__ == '__main__':
    #图片地址
    path = 'C:/Users/m1309/Desktop/odemo-pic-7.jpg'
    with open(path, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        s = base64_data.decode()
    answer = get_content(s)
    print(answer)
