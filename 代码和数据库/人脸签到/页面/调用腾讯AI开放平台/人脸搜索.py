import requests
import 人脸搜索_sign
import base64
import tkinter as tk
from tkinter import filedialog


def get_content(path, class_id):

    with open(path, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        img = base64_data.decode()


    # 人脸识别的API地址
    url = "https://api.ai.qq.com/fcgi-bin/face/face_faceidentify"
    # 获取请求参数
    payload = 人脸搜索_sign.get_params(img, class_id)

    r = requests.post(url, data=payload)
    return r.json()


if __name__ == '__main__':

    path = 'C:/Users/m1309/Desktop/测试图集/test_2.jpg'
    class_id = 'test'
    answer = get_content(path, class_id)

    print(answer)
