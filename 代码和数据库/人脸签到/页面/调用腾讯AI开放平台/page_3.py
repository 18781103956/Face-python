import tkinter
import tkinter.filedialog
from tkinter import ttk
import time
import Mydatabase

from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import requests
import base64
import 多人脸检测
import 多人脸检测_sign
import 人脸搜索
import 人脸搜索_sign
import 剪切图片
import 放大图片

# 覆盖窗口
def Cover(win):
    label_bg = tkinter.Label(win, text="", bg="#F7F7F7")
    label_bg.place(x=0, y=0, width=1000, height=1000)


def page_3_win(body, class_id):
    body.title("班级签到: "+class_id)
    body.maxsize(800, 400)
    body.minsize(800, 400)

    # 覆盖函数
    Cover(body)
    #返回主页
    import page_1
    b_3 = Button(body, text='返回主页', font=('黑体', 15), command=lambda: page_1.page_win(body))
    b_3.place(x=680, y=340, width=100, height=50)

    # 表头
    tree = ttk.Treeview(body)
    tree["columns"] = ("姓名", "性别", "是否签到")
    tree.column("姓名", width=100)  # 表示列,不显示
    tree.column("性别", width=100)
    tree.column("是否签到", width=150)

    tree.heading("姓名", text="姓名")  # 显示表头
    tree.heading("性别", text="性别")
    tree.heading("是否签到", text="是否签到")
    # 调用数据库传送班级学生数据
    result = Mydatabase.find_Allstudent(class_id)
    print(result)

    num = 0 #学生数
    for item in result:
        if float(item[3]) >= 75.0:
            tree.insert("", 0, text=str(item[0]), values=(item[1], item[2], "                    是"))  # 插入数据，
        else:
            tree.insert("", 0, text=str(item[0]), values=(item[1], item[2], "                    否"))
        num = num + 1
    tree.place(x=50, y=40, width=710, height=250)
    body.mainloop()


if __name__ == '__main__':
    win = tkinter.Tk()
    page_3_win(win, '111')
    win.mainloop()









