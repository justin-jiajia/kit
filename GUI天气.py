from tkinter import *
from tkinter.messagebox import *
import requests

key = "81f52a7266344015bd30eef507e3c8fd"

weather = Tk()
weather.title("天气")
weather.resizable(width=False, height=False)
try:
    r = requests.get("https://devapi.qweather.com/v7/weather/now", params={"key": key,
                                                                           "location": "101190808"})
except:
    update_time = Label(weather, text="天气加载失败", font=('楷体 常规', 18))
    update_time.grid(column=0, row=1)
    showerror("错误", "网络连接出错，加载天气失败！")
else:
    w = r.json()
    update_time = Label(weather, text="更新日期："+w["now"]["obsTime"][:-6])
    update_time.grid(column=0, row=0)

    top = Frame(weather)
    top.grid(column=0, row=1)
    text = Label(top, text="天气："+w["now"]["text"]+"\n温度："+w["now"]["temp"]+"℃")
    text.grid(column=1, row=0)

    x = Frame(weather)
    x.grid(column=0, row=2)
    feels = Label(x, text="体感温度："+w["now"]["feelsLike"])
    feels.grid(column=0, row=0)
    windDir = Label(x, text="风向："+w["now"]["windDir"])
    windDir.grid(column=1, row=0)

weather.mainloop()
