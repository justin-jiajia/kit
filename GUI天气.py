from tkinter import *
from tkinter.messagebox import *
import requests
import json

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
    w = json.loads(r.content)
    update_time = Label(weather, text="更新日期："+w["now"]["obsTime"][:-6])
    update_time.grid(column=0, row=0)

    top = Frame(weather)
    top.grid(column=0, row=1)
    text = Label(top, text="天气："+w["now"]["text"]+"\n温度："+w["now"]["temp"]+"℃")
    text.grid(column=1, row=0)

    x = Frame(weather)
    x.grid(column=0, row=2)
    feels = Label(x, text="体感温度："+w["now"]["feelsLike"]+"℃")
    feels.grid(column=0, row=0)
    windDir = Label(x, text="风向："+w["now"]["windDir"])
    windDir.grid(column=1, row=0)

    humidity = Label(x, text="相对湿度："+w["now"]["humidity"]+"%")
    humidity.grid(column=0, row=1)
    windScale = Label(x, text="风力等级："+w["now"]["windScale"])
    windScale.grid(column=1, row=1)

    dew = Label(x, text="露点温度："+w["now"]["dew"]+"℃")
    dew.grid(column=0, row=2)
    windSpeed = Label(x, text="风速："+w["now"]["windSpeed"]+"公里/小时")
    windSpeed.grid(column=1, row=2)

    pressure = Label(x, text="大气压强："+w["now"]["pressure"]+"百帕")
    pressure.grid(column=0, row=3)
    vis = Label(x, text="能见度："+w["now"]["vis"]+"公里")
    vis.grid(column=1, row=3)

weather.mainloop()
