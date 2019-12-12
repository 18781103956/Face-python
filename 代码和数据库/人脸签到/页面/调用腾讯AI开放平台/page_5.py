import tkinter
import Mydatabase
import tkinter.messagebox

def Cover(win):
    label_bg = tkinter.Label(win, text="", bg="#F7F7F7")
    label_bg.place(x=0, y=0, width=900, height=380)

def look_stu_infor(sno, cno, infor_text):
    data = Mydatabase.SQl_data()
    result = data.Find_stu(sno, cno)
    infor_text.set(result)


def updata_stu(sno, num):
    data = Mydatabase.SQl_data()
    data.Updata_stu_data(sno, num)
    tkinter.messagebox.showinfo("提示！", "确定修改")

def win(win):
    global infor
    win.title("face")
    win.geometry("400x300+600+200")
    Cover(win)

    sno_text = tkinter.StringVar()
    lb_sno = tkinter.Label(win, text="输入学号:")
    lb_sno.place(x=0, y=0, height=30, width=60)
    in_sno = tkinter.Entry(win, textvariable=sno_text)
    in_sno.place(x=90, y=0, height=20, width=120)

    cno_text = tkinter.StringVar()
    lb_cno = tkinter.Label(win, text="输入课程号：")
    lb_cno.place(x=0, y=30, height=30)
    in_cno = tkinter.Entry(win, textvariable=cno_text)
    in_cno.place(x=90, y=30, height=20, width=120)

    infor_text = tkinter.StringVar()
    button_cno = tkinter.Button(win, text="查询", command=lambda: look_stu_infor(sno_text.get(), cno_text.get(), infor_text))
    button_cno.place(x=250, y=30, height=20)


    lb_infor = tkinter.Label(win, text="查询结果：")
    lb_infor.place(x=0, y=60, height=30)
    in_infor = tkinter.Entry(win, textvariable=infor_text)
    in_infor.place(x=90, y=60, height=60, width=200)

    data_text = tkinter.StringVar()
    lb_updata = tkinter.Label(win, text="考勤修改:")
    lb_updata.place(x=0, y=130, height=30)
    in_updata = tkinter.Entry(win, textvariable=data_text)
    in_updata.place(x=90, y=130, height=20, width=120)

    botton = tkinter.Button(win, text="确定修改", command=lambda: updata_stu(sno_text.get(), data_text.get()))
    botton.place(x=0, y=180)
    botton_out =tkinter.Button(win, text="退出", command=win.quit)
    botton_out.place(x=200, y=180)

    win.mainloop()
if __name__ == '__main__':
    win_1 = tkinter.Tk()
    win(win_1)