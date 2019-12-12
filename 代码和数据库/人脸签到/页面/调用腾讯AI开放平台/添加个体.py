import requests
import 添加个体_sign
import base64


def get_content(path, group_id, person_id, person_name):

    with open(path, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        img = base64_data.decode()

    # 人脸识别的API地址
    url = "https://api.ai.qq.com/fcgi-bin/face/face_newperson"
    # 获取请求参数
    payload = 添加个体_sign.get_params(img, group_id, person_id, person_name)

    r = requests.post(url, data=payload)
    return r.json()


if __name__ == '__main__':

    path = 'C:/Users/m1309/Desktop/test_3.jpg'

    answer = get_content(path, 'test', 'test_3', '1')

    print(answer)