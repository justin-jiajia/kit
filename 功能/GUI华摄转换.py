from tkinter import *
from tkinter.messagebox import *

from 函数 import 华摄转换

# 新建窗口，设定标题
hszh = Tk()
hszh.title('华摄转换')
hszh.resizable(width=False, height=False)


def sysm():
    showinfo('使用说明', '期待！')


def print_ctof():
    c_ctof_int = 1  # 添加此句是为了防止后面报错 局部变量 'c_ctof_int' 可能在赋值前引用
    try:
        c_ctof_int = float(c_ctof.get())
    except ValueError:
        showerror('错误', '请输入数字！')
    else:
        f_ctof.delete(1.0, END)
        f_ctof.insert('end', 华摄转换.ctof(c_ctof_int))


def print_ftoc():
    f_ctof_int = 0  # 添加此句是为了防止后面报错 局部变量 'f_ctof_int' 可能在赋值前引用
    try:
        f_ctof_int = float(f_ftoc.get())
    except ValueError:
        showerror('错误', '请输入数字！')
    else:
        c_ftoc.delete(1.0, END)
        c_ftoc.insert('end', 华摄转换.ftoc(f_ctof_int))


t = Label(hszh, text='华摄转换')
t.grid(row=1, column=1)
b = Button(hszh, text='使用说明', command=sysm)
b.grid(row=1, column=2)
ctof_t = Label(hszh, text='摄氏度转华氏度')
ctof_t.grid(row=2, column=1)
ftoc_t = Label(hszh, text='华氏度转摄氏度')
ftoc_t.grid(row=2, column=2)

ctof = Frame(hszh)
ctof.grid(row=3, column=1)

sry_ctof = Frame(ctof)
sry_ctof.grid(column=0, row=1)

tip1 = Label(sry_ctof, text='摄氏度:')
tip1.grid(column=0, row=0)
c_ctof = Entry(sry_ctof, width=17)
c_ctof.grid(column=1, row=0)
ctof_b = Button(sry_ctof, text='转换', command=print_ctof)
ctof_b.grid(column=2, row=0)

jg_ctof = Frame(ctof)
jg_ctof.grid(column=0, row=2)
tip2 = Label(jg_ctof, text='结果:')
tip2.grid(column=0, row=0)
f_ctof = Text(jg_ctof, height=1, width=25)
f_ctof.grid(column=1, row=0)

ftoc = Frame(hszh)
ftoc.grid(row=3, column=2)

sry_ftoc = Frame(ftoc)
sry_ftoc.grid(column=0, row=1)
tip1 = Label(sry_ftoc, text='华氏度:')
tip1.grid(column=0, row=0)
f_ftoc = Entry(sry_ftoc, width=17)
f_ftoc.grid(column=1, row=0)
ftoc_b = Button(sry_ftoc, text='转换', command=print_ftoc)
ftoc_b.grid(column=2, row=0)

jg_ftoc = Frame(ftoc)
jg_ftoc.grid(column=0, row=2)
tip2 = Label(jg_ftoc, text='结果:')
tip2.grid(column=0, row=0)
c_ftoc = Text(jg_ftoc, height=1, width=25)
c_ftoc.grid(column=1, row=0)
hszh.mainloop()
