from tkinter import *
from tkinter.messagebox import *

jsq = Tk()
jsq.title("计算器")
jsq.resizable(width=False, height=False)
jsq.geometry('160x90+10+100')


def sysm():
    showinfo("使用说明", "期待！")


def js():
    if not ss.get():
        try:
            jg_int = eval(ss.get())
        except (NameError, TclError, SyntaxError):
            showerror("错误", "您输入的内容有误，请检查！")
        else:
            jg.delete(1.0, END)
            jg.insert("end", jg_int)
    else:
        showerror("错误", "请输入内容")


tittle = Frame(jsq)
tittle.grid(column=0, row=0)
t = Label(tittle, text="计算器")
t.grid(column=1, row=0)
zwf = Label(tittle, text="             ")
zwf.grid(column=0, row=0)
b = Button(tittle, text="使用说明", width=7, command=sysm)
b.grid(column=2, row=0)

sr = Frame(jsq)
sr.grid(column=0, row=1)
ss = Entry(sr, width=17)
ss.grid(column=0, row=0)
js_b = Button(sr, text="计算", width=4, command=js)
js_b.grid(column=1, row=0)

jg_f = Frame(jsq)
jg_f.grid(column=0, row=2)
tip1 = Label(jg_f, text="结果:")
tip1.grid(column=0, row=0)
jg = Text(jg_f, height=1, width=18)
jg.grid(column=1, row=0)

jsq.mainloop()
