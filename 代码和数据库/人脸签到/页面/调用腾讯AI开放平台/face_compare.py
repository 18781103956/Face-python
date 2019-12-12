import requests
import facecompare_sign
import base64


def get_content(img_a, img_b):
    # 功能 API地址
    url = "https://api.ai.qq.com/fcgi-bin/face/face_facecompare"
    # 获取请求参数
    payload = facecompare_sign.get_params(img_a, img_b)

    r = requests.post(url, data=payload)
    return r.json()


if __name__ == '__main__':
    path_a = 'image/f_1.png'
    path_b = 'image/f_1.png'


    with open(path_a, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        s_a = base64_data.decode()

    with open(path_b, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        s_b = base64_data.decode()


    answer = get_content(s_a, s_b)
    print(answer)
