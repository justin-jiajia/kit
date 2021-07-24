from tkinter import *
from tkinter.messagebox import *

from 函数 import 替换式密码

# 新建窗口，设定标题
thsmm = Tk()
thsmm.title("替换式密码")
thsmm.resizable(width=False, height=False)


def sysm():
    showinfo("使用说明", "期待！")


def jiami():
    yi_jia_int = 1  # 添加此句是为了防止后面报错 局部变量 'yi_jia_int' 可能在赋值前引用
    try:
        yi_jia_int = int(yi_jia.get())
    except ValueError:
        showerror("错误", "请输入数字！")
    finally:
        mi_jia.delete(1.0, END)
        mi_jia.insert("end", 替换式密码.jiami(ming_jia.get(), yi_jia_int))


def jiemi():
    yi_jie_int = 0  # 添加此句是为了防止后面报错 局部变量 'yi_jie_int' 可能在赋值前引用
    try:
        yi_jie_int = int(yi_jie.get())
    except ValueError:
        showerror("错误", "请输入数字！")
    finally:
        ming_jie.delete(1.0, END)
        ming_jie.insert("end", 替换式密码.jiemi(mi_jie.get(), yi_jie_int))


t = Label(thsmm, text="替换式密码")
t.grid(row=1, column=1)
b = Button(thsmm, text="使用说明", command=sysm)
b.grid(row=1, column=2)
jia_t = Label(thsmm, text="加密")
jia_t.grid(row=2, column=1)
jie_t = Label(thsmm, text="解密")
jie_t.grid(row=2, column=2)
jia = Frame(thsmm)
jia.grid(row=3, column=1)
srm_jia = Frame(jia)
srm_jia.grid(column=0, row=0)
tip1 = Label(srm_jia, text="明文:")
tip1.grid(column=0, row=0)
ming_jia = Entry(srm_jia, show=None, width=25)
ming_jia.grid(column=1, row=0)
sry_jia = Frame(jia)
sry_jia.grid(column=0, row=2)
tip2 = Label(sry_jia, text="移位值:")
tip2.grid(column=0, row=0)
yi_jia = Entry(sry_jia, width=17)
yi_jia.grid(column=1, row=0)
jia_b = Button(sry_jia, text="加密", command=jiami)
jia_b.grid(column=2, row=0)
jg_jia = Frame(jia)
jg_jia.grid(column=0, row=3)
tip3 = Label(jg_jia, text="结果:")
tip3.grid(column=0, row=0)
mi_jia = Text(jg_jia, height=1, width=25)
mi_jia.grid(column=1, row=0)
jie = Frame(thsmm)
jie.grid(row=3, column=2)
srm_jie = Frame(jie)
srm_jie.grid(column=0, row=1)
tip1 = Label(srm_jie, text="密文:")
tip1.grid(column=0, row=0)
mi_jie = Entry(srm_jie, show=None, width=25)
mi_jie.grid(column=1, row=0)
sry_jie = Frame(jie)
sry_jie.grid(column=0, row=2)
tip2 = Label(sry_jie, text="移位值:")
tip2.grid(column=0, row=0)
yi_jie = Entry(sry_jie, width=17)
yi_jie.grid(column=1, row=0)
jie_b = Button(sry_jie, text="解密", command=jiemi)
jie_b.grid(column=2, row=0)
jg_jie = Frame(jie)
jg_jie.grid(column=0, row=3)
tip3 = Label(jg_jie, text="结果:")
tip3.grid(column=0, row=0)
ming_jie = Text(jg_jie, height=1, width=25)
ming_jie.grid(column=1, row=0)
thsmm.mainloop()
