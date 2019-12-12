import requests
import 多人脸检测_sign
import base64
from PIL import Image


def get_content(path):
    print("zzzz")
    print(path)

    with open(path, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        img = base64_data.decode()

    # 人脸识别的API地址
    url = "https://api.ai.qq.com/fcgi-bin/face/face_detectmultiface"
    # 获取请求参数
    payload = 多人脸检测_sign.get_params(img)

    r = requests.post(url, data=payload)
    return r.json()

if __name__ == '__main__':

    path = "C:/Users/m1309/Desktop/测试图集/" + 'class_1.jpg'

    answer = get_content(path)

    print(answer)

