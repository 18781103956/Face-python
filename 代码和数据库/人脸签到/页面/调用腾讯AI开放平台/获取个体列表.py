import requests
import 获取个体列表_sign
import base64


def get_content(group_id):
    # 人脸识别的API地址
    url = "https://api.ai.qq.com/fcgi-bin/face/face_getpersonids"
    # 获取请求参数
    payload = 获取个体列表_sign.get_params(group_id)

    r = requests.post(url, data=payload)
    return r.json()

if __name__ == '__main__':

    group_id = '001'
    answer = get_content(group_id)
    print(answer)