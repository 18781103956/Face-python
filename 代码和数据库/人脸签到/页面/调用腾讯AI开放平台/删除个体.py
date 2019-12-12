import requests
import 删除个体_sign
import base64


def get_content(person_id):
    # 人脸识别的API地址
    url = "https://api.ai.qq.com/fcgi-bin/face/face_delperson"
    # 获取请求参数
    payload = 删除个体_sign.get_params(person_id)

    r = requests.post(url, data=payload)
    return r.json()


if __name__ == '__main__':

    person_id = 'test_3'

    answer = get_content(person_id)

    print(answer)