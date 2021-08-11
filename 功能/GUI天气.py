from tkinter import *
from tkinter.messagebox import *
import requests

key = '81f52a7266344015bd30eef507e3c8fd'

weather = Tk()
weather.title('天气')
weather.resizable(width=False, height=False)
try:
    r = requests.get('https://devapi.qweather.com/v7/weather/now', params={'key': key,
                                                                           'location': '101190808'})
except requests.exceptions.ConnectionError:
    update_time = Label(weather, text='天气加载失败', font=('楷体 常规', 18))
    update_time.grid(column=0, row=1)
    showerror('错误', '网络连接出错，加载天气失败！')
else:
    w = r.json()
    update_time = Label(weather, text='更新日期：'+w['now']['obsTime'])
    update_time.grid(column=0, row=0)

    now = Frame(weather)
    now.grid(column=0, row=2)

    img = PhotoImage(file='WeatherIcon/彩色/'+w['now']['icon']+'.png')
    # img = PhotoImage(file='WeatherIcon/黑白/'+w['now']['icon']+'.png')
    # img = PhotoImage(file='WeatherIcon/实况/'+w['now']['icon']+'.png')
    
    w_img = Label(now, image=img)
    w_img.grid(column=0, row=0)
    text = Label(now, text='天气：'+w['now']['text']+'\n温度：'+w['now']['temp']+'℃')
    text.grid(column=1, row=0)

    feels = Label(now, text='体感温度：'+w['now']['feelsLike']+'℃')
    feels.grid(column=0, row=1)
    windDir = Label(now, text='风向：'+w['now']['windDir'])
    windDir.grid(column=1, row=1)

    humidity = Label(now, text='相对湿度：'+w['now']['humidity']+'%')
    humidity.grid(column=0, row=2)
    windScale = Label(now, text='风力等级：'+w['now']['windScale'])
    windScale.grid(column=1, row=2)

    dew = Label(now, text='露点温度：'+w['now']['dew']+'℃')
    dew.grid(column=0, row=3)
    windSpeed = Label(now, text='风速：'+w['now']['windSpeed']+'公里/小时')
    windSpeed.grid(column=1, row=3)

    pressure = Label(now, text='大气压强：'+w['now']['pressure']+'百帕')
    pressure.grid(column=0, row=4)
    vis = Label(now, text='能见度：'+w['now']['vis']+'公里')
    vis.grid(column=1, row=4)

weather.mainloop()
