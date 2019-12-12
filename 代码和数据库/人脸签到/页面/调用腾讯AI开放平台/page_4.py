import tkinter
import tkinter.filedialog
import time
import Mydatabase
from PIL import Image, ImageTk
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
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
import tkinter.messagebox

def choosepic_1():
    global path_1
    global e_1
    global l_1
    global path_


    path_ = askopenfilename()
    path_1.set(path_)
    img_open = Image.open(path_)
    x, y = img_open.size
    x = int(x*0.8)
    y = int(y*0.8)
    img_open = img_open.resize((x, y), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img_open)
    l_1.config(image=img)
    l_1.image = img

# 覆盖窗口
def Cover(win):
    label_bg = tkinter.Label(win, text="", bg="#F7F7F7")
    label_bg.place(x=0, y=0, width=1000, height=1000)

# 处理数据
def take_date(win, path, stu_id, stu_name, stu_sex, stu_class):

    import 添加个体
    answer = 添加个体.get_content(path, stu_class, stu_id, stu_name)
    tkinter.messagebox.showinfo("提示！", "请耐心等待添加！！！")

    if answer['ret'] == 0:
        tkinter.messagebox.showinfo("提示！", "添加成功！！！")


    import Mydatabase
    Mydatabase.insert_student(stu_id, stu_name, stu_sex, stu_class)

    import page_3
    page_3.page_3_win(win, stu_class)


def delete(body, stu_id):
    import 删除个体
    answer = 删除个体.get_content(stu_id)
    tkinter.messagebox.showinfo("提示！", "请耐心等待删除！！！")

    if answer['ret'] == 0:
        tkinter.messagebox.showinfo("提示！", "删除成功！！！")

    import Mydatabase
    Mydatabase.del_student(stu_id)



def page_4_win(body):
    body.title("添加/删除学生: ")
    body.maxsize(700, 500)
    body.minsize(700, 500)


    # 覆盖函数
    Cover(body)

    global path_1
    global path_
    global e_1
    global l_1

    path_1 = StringVar()
    b_1 = Button(body, text='请上传学生本人照片', command=choosepic_1)
    b_1.place(x=20, y=15, width=120, height=25)

    e_1 = Entry(body, state='readonly', text=path_1)
    e_1.place(x=150, y=15, width=250, height=25)

    l_1 = Label(body, bg="#FFFFFF")
    l_1.place(x=20, y=55, width=380, height=400)

    # 添加学号
    label = tkinter.Label(body, text="学  号:", font=('微软雅黑', 12), fg='black', bg="#F7F7F7")
    label.place(x=400, y=20)
    entry_1 = tkinter.Entry(body)
    entry_1.place(x=480, y=20)

    # 添加姓名
    label_2 = tkinter.Label(body, text="姓  名:", font=('微软雅黑', 12), fg='black', bg="#F7F7F7")
    label_2.place(x=400, y=50)
    entry_2 = tkinter.Entry(body)
    entry_2.place(x=480, y=50)

    # 添加性别
    label_3 = tkinter.Label(body, text="性  别:", font=('微软雅黑', 12), fg='black', bg="#F7F7F7")
    label_3.place(x=400, y=80)
    entry_3 = tkinter.Entry(body)
    entry_3.place(x=480, y=80)

    # 所在班级
    label_4 = tkinter.Label(body, text="所在班级:", font=('微软雅黑', 12), fg='black', bg="#F7F7F7")
    label_4.place(x=400, y=110)
    entry_4 = tkinter.Entry(body)
    entry_4.place(x=480, y=110)


    botton = tkinter.Button(body, text='添加学生', font=('微软雅黑', 12), command=lambda: take_date(body, str(path_), entry_1.get(), entry_2.get(), entry_3.get(), entry_4.get() ))
    botton.place(x=440, y=190)

    botton_1 = tkinter.Button(body, text='删除学生', font=('微软雅黑', 12), command=lambda: delete(body, entry_1.get()))
    botton_1.place(x=540, y=190)

    label_5 = tkinter.Label(body, text="*提示*删除学生只需要输入学号编号", font=('微软雅黑', 12), fg='gray', bg="#F7F7F7")
    label_5.place(x=400, y=230)

    import page_1
    b_3 = Button(body, text='返回主页', font=('黑体', 15), command=lambda: page_1.page_win(body))
    b_3.place(x=580, y=400, width=100, height=50)


if __name__ == '__main__':
    win = tkinter.Tk()
    page_4_win(win)
    win.mainloop()




