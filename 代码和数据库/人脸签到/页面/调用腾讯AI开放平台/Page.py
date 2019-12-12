import tkinter
import tkinter.messagebox
import Mydatabase


# 登陆界面
def Log_register():
    win = tkinter.Tk()
    win.title("登陆页面")
    win.maxsize(900, 350)
    win.minsize(900, 350)

    #背景
    canvas = tkinter.Canvas(win)
    image_file = tkinter.PhotoImage(file='timg.png')
    image = canvas.create_image(0, 0, anchor='nw', image=image_file)
    canvas.place(x=0, y=20, height=420, width=619)

    #全局变量
    global name_text
    global pwd_text

    #加入Label_title
    lp_title = tkinter.Label(win, text='课堂签到', font=("Arial Black", 22), fg='#32cd99')
    lp_title.place(x=625, y=150)

    #add copyright_lable_
    bottom_lable = tkinter.Label(win, text='Face @ 天津大学仁爱学院')
    bottom_lable.place(x=280, y=360)

    #加入name
    name_text = tkinter.Variable()
    name_lb = tkinter.Label(win, text='用户名:', font=('微软雅黑', 13))
    name_lb.place(x=625, y=200)
    name_input = tkinter.Entry(win, textvariable=name_text, width=20)
    name_input.place(x=685, y=200)


    #加入密码
    pwd_text = tkinter.Variable()
    pwd_lb = tkinter.Label(win, text='密码:', font=('微软雅黑', 13))
    pwd_lb.place(x=625, y=235)
    pwd_input = tkinter.Entry(win, show='*', textvariable=pwd_text, width=20)
    pwd_input.place(x=685, y=235)

    # 登录按钮
    login_button = tkinter.Button(win, text='登录', font=('微软雅黑', 12), command=lambda: login_page(win))
    login_button.place(x=770, y=280)

    # 退出按钮
    quit_button = tkinter.Button(win, text='退出', font=('微软雅黑', 12), command=win.quit)
    quit_button.place(x=700, y=280)

    win.mainloop()

def login_page(win):
    global name_text
    global pwd_text

    #验证账号是否正确  调用Judge_account
    result = Judge_account(name_text.get(), pwd_text.get())

    if result == True:
        tkinter.messagebox.showinfo("提示！", "登录成功")
        # 局部调用
        import page_1
        page_1.page_win(win)
    else:
        tkinter.messagebox.showinfo("提示！", "账户或密码错误")


# 验证输入的账号号和密码是否正确
def Judge_account(id, password):   #id-账号, password-密码
    import Mydatabase
    x = Mydatabase.l_data(id)
    print("xxx",x)
    if x[0][0] == password:
        return True
    else:
        return False


if __name__ == '__main__':
    #执行类
    Log_register()


