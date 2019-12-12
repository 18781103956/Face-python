import tkinter
import Mydatabase
import tkinter.messagebox

#覆盖窗口
def Cover(win):
    label_bg = tkinter.Label(win, text="", bg="#F7F7F7")
    label_bg.place(x=0, y=0, width=900, height=380)

#确定进入下一页面
def change_win(win):
    entry = tkinter.Entry(win)
    entry.place(x=560, y=280)

    #局部调用
    import page_2
    botton = tkinter.Button(win, text="进入班级", font=('微软雅黑', 12), command=lambda: page_2.page_2_win(win, entry.get()))
    botton.place(x=720, y=270)

    import page_4
    #page_4.page_4_win(win)
    botton_2 = tkinter.Button(win, text="添加学生", font=('微软雅黑', 12), command=lambda: page_4.page_4_win(win))
    botton_2.place(x=720, y=320)

#该页面主要布局
def switch(win):
    # 表头
    class_label = tkinter.Label(win, text="班 号              人 数             任课老师", font=('微软雅黑', 13), fg='blue', bg="#F7F7F7")
    class_label.place(x=0, y=0)

    # 班级表
    lbx = tkinter.StringVar()
    lb = tkinter.Listbox(win, selectmode=tkinter.SINGLE, listvariable=lbx, font=('黑体', 15), bg="#FFFFFF")
    lb.place(x=0, y=30, height=300, width=400)

    # 调用数据库传送班级数据
    result = Mydatabase.find_AllClass()
    print(result)
    for item in result:
        temp = item[0] + "         " + item[1] + "        " + item[2]
        lb.insert(tkinter.END, temp)

    # 添加新的班级信息
    label = tkinter.Label(win, text="班  号:", font=('微软雅黑', 15), fg='black', bg="#F7F7F7")
    label.place(x=400, y=25)
    entry_1 = tkinter.Entry(win)
    entry_1.place(x=500, y=30)

    # 添加班级人数
    label_3 = tkinter.Label(win, text="班级人数:", font=('微软雅黑', 15), fg='black', bg="#F7F7F7")
    label_3.place(x=400, y=75)
    entry_3 = tkinter.Entry(win)
    entry_3.place(x=500, y=80)

    # 添加任课老师
    label_4 = tkinter.Label(win, text="任课老师:", font=('微软雅黑', 15), fg='black', bg="#F7F7F7")
    label_4.place(x=400, y=125)
    entry_4 = tkinter.Entry(win)
    entry_4.place(x=500, y=130)

    label_5 = tkinter.Label(win, text="请输入签到班号:", font=('微软雅黑', 15), fg='black', bg="#F7F7F7")
    label_5.place(x=400, y=275)

    botton = tkinter.Button(win, text='新建班级', font=('微软雅黑', 12), command=lambda: create(win, (entry_1.get(), entry_3.get(), entry_4.get())))
    botton.place(x=480, y=170)

    botton_1 = tkinter.Button(win, text='删除班级', font=('微软雅黑', 12), command=lambda: delete(win, entry_1.get()))
    botton_1.place(x=580, y=170)

    label_5 = tkinter.Label(win, text="*提示*删除班级只需要输入班级编号", font=('微软雅黑', 12), fg='gray', bg="#F7F7F7")
    label_5.place(x=480, y=210)

#新建班级
def create(win, val):
    result = Mydatabase.Add_class(val)
    tkinter.messagebox.showinfo("提示！", "新建成功")
    page_win(win)

#删除班级
def delete(win, val):
    result = Mydatabase.Delete_class(val)
    tkinter.messagebox.showinfo("提示！", "删除成功")
    page_win(win)


def page_win(win):
    win.title("班级显示")
    win.maxsize(900, 380)
    win.minsize(900, 380)

    # 覆盖函数
    Cover(win)

    # 该页面主要布局
    switch(win)

    change_win(win)




if __name__ == '__main__':
    win = tkinter.Tk()
    page_win(win)
    win.mainloop()

