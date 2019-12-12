import requests
import md5sign
import base64


def get_content(plus_item):
    # 功能 API地址
    url = "https://api.ai.qq.com/fcgi-bin/face/face_detectface"
    # 获取请求参数
    payload = md5sign.get_params(plus_item)

    r = requests.post(url, data=payload)
    return r.json()


if __name__ == '__main__':
    path = './image/image.jpg'
    with open(path, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        s = base64_data.decode()
    answer = get_content(s)
    print(answer)
