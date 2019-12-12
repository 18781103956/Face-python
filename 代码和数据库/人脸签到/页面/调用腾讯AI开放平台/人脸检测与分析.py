import requests
import md5sign
import base64
import tkinter as tk
from tkinter import filedialog



def get_content(plus_item):
    # 人脸识别的API地址
    url = "https://api.ai.qq.com/fcgi-bin/face/face_detectface"
    # 获取请求参数
    payload = md5sign.get_params(plus_item)

    r = requests.post(url, data=payload)
    return r.json()


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askopenfilename()

   # path = './image/image.jpg'
    with open(path, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        s = base64_data.decode()
    answer = get_content(s)
    print(answer)

