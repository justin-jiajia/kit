import json
from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *

import requests

from 函数 import 华摄转换
from 函数 import 替换式密码

# 新建窗口，设定标题、图标
tk = Tk()
tk.title("工具箱")
tk.resizable(width=False, height=False)
# home.iconbitmap("x.ico")

tab = Notebook()
tab.grid(column=0, row=0)

home = Frame(tab)
home.grid(column=0, row=0)
thsmm = Frame(tab)
thsmm.grid(column=0, row=0)
jsq = Frame(tab)
jsq.grid(column=0, row=0)
hszh = Frame(tab)
hszh.grid(column=0, row=0)

tab.add(home, text="首页")
tab.add(thsmm, text="替换式文本加解密")
tab.add(hszh, text="华摄转换")
tab.add(jsq, text="计算器")

# 首页的程序
# 获取一句诗
url = "https://v1.hitokoto.cn"
param = {"c": "i"}
try:
    r = requests.get(url, params=param)
except:
    text1 = Label(home, text="诗词加载失败", font=('楷体 常规', 18))
    text1.grid(column=0, row=1)
    showerror("错误", "网络连接出错，加载每日诗词失败！")
else:
    i = json.loads(r.content)
    c = "——" + i["from_who"] + "《" + i["from"] + "》"  # 格式化出处、来源
    # 将诗词放在屏幕上
    text1 = Label(home, text=i["hitokoto"], font=('楷体 常规', 18))
    text1.grid(column=0, row=1)
    # 将出处、来源放在屏幕上
    text2 = Label(home, text=c, font=("", 18))
    text2.grid(column=0, row=2)


# 替换式密码的程序
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
jia_b = Button(sry_jia, text="加密", width=4, command=jiami)
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
jie_b = Button(sry_jie, text="解密", width=4, command=jiemi)
jie_b.grid(column=2, row=0)
jg_jie = Frame(jie)
jg_jie.grid(column=0, row=3)
tip3 = Label(jg_jie, text="结果:")
tip3.grid(column=0, row=0)
ming_jie = Text(jg_jie, height=1, width=25)
ming_jie.grid(column=1, row=0)


# 华摄转换的程序
def sysm():
    showinfo("使用说明", "期待！")


def print_ctof():
    c_ctof_int = 1  # 添加此句是为了防止后面报错 局部变量 'c_ctof_int' 可能在赋值前引用
    try:
        c_ctof_int = float(c_ctof.get())
    except ValueError:
        showerror("错误", "请输入数字！")
    finally:
        f_ctof.delete(1.0, END)
        f_ctof.insert("end", 华摄转换.ctof(c_ctof_int))


def print_ftoc():
    f_ctof_int = 0  # 添加此句是为了防止后面报错 局部变量 'f_ctof_int' 可能在赋值前引用
    try:
        f_ctof_int = float(f_ftoc.get())
    except ValueError:
        showerror("错误", "请输入数字！")
    finally:
        c_ftoc.delete(1.0, END)
        c_ftoc.insert("end", 华摄转换.ftoc(f_ctof_int))


t = Label(hszh, text="华摄转换")
t.grid(row=1, column=1)
b = Button(hszh, text="使用说明", width=7, command=sysm)
b.grid(row=1, column=2)
ctof_t = Label(hszh, text="摄氏度转华氏度")
ctof_t.grid(row=2, column=1)
ftoc_t = Label(hszh, text="华氏度转摄氏度")
ftoc_t.grid(row=2, column=2)

ctof = Frame(hszh)
ctof.grid(row=3, column=1)

sry_ctof = Frame(ctof)
sry_ctof.grid(column=0, row=1)

tip1 = Label(sry_ctof, text="摄氏度:")
tip1.grid(column=0, row=0)
c_ctof = Entry(sry_ctof, width=17)
c_ctof.grid(column=1, row=0)
ctof_b = Button(sry_ctof, text="转换", width=4, command=print_ctof)
ctof_b.grid(column=2, row=0)

jg_ctof = Frame(ctof)
jg_ctof.grid(column=0, row=2)
tip2 = Label(jg_ctof, text="结果:")
tip2.grid(column=0, row=0)
f_ctof = Text(jg_ctof, height=1, width=25)
f_ctof.grid(column=1, row=0)

ftoc = Frame(hszh)
ftoc.grid(row=3, column=2)

sry_ftoc = Frame(ftoc)
sry_ftoc.grid(column=0, row=1)
tip1 = Label(sry_ftoc, text="华氏度:")
tip1.grid(column=0, row=0)
f_ftoc = Entry(sry_ftoc, width=17)
f_ftoc.grid(column=1, row=0)
ftoc_b = Button(sry_ftoc, text="转换", width=4, command=print_ftoc)
ftoc_b.grid(column=2, row=0)

jg_ftoc = Frame(ftoc)
jg_ftoc.grid(column=0, row=2)
tip2 = Label(jg_ftoc, text="结果:")
tip2.grid(column=0, row=0)
c_ftoc = Text(jg_ftoc, height=1, width=25)
c_ftoc.grid(column=1, row=0)


# 计算器的程序
def sysm():
    showinfo("使用说明", "期待！")


def js():
    if not ss.get() == "":
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

tk.mainloop()
