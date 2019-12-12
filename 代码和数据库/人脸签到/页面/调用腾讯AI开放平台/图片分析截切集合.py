import requests
import base64
from PIL import Image
import 多人脸检测
import 多人脸检测_sign
import 人脸搜索
import 人脸搜索_sign
import 剪切图片
import 放大图片
import time

def Find_person(path, path_goal, class_id):
    img_type = path[-4:]
    class_name = 'test_'
    ls = []

    ans_1 = 多人脸检测.get_content(path)

    if ans_1['ret'] == 0:
        face_site = ans_1['data']['face_list']
        ctor = 0

        for i in face_site:
            x1 = int(i['x1']*0.95)
            y1 = int(i['y1']*0.95)
            x2 = int(i['x2']*1.05)
            y2 = int(i['y2']*1.05)

            temp_path_goal = path_goal + class_name + str(ctor) + img_type
            ctor = ctor + 1
            #print(temp_path_goal)

            剪切图片.crop_img(path, x1, y1, x2, y2, temp_path_goal)
            放大图片.resize_img(temp_path_goal, temp_path_goal)
            ans_2 = 人脸搜索.get_content(temp_path_goal, class_id)

            if ans_2['ret'] == 0:
                simi_person = ans_2['data']['candidates'][0]

                ls.append([simi_person['person_id'], simi_person['confidence']])
                #print(simi_person)

                #print(simi_person['person_id'], '--', simi_person['confidence'])
                time.sleep(1)


        #print(face_site)

    else:

        print("图片分析失败，请重新提交！！！")

    return ls

if __name__ == '__main__':

    path = 'C:/Users/m1309/Desktop/测试图集/ai.png'
    class_id = 'test'
    path_goal = 'C:/Users/m1309/Desktop/'
    ans = Find_person(path, path_goal, class_id)


    for i in ans:
        print(i[0], ':', i[1])

