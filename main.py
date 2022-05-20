#!/usr/bin/python3
import tkinter as tk
import pyautogui,time,webbrowser
window=tk.Tk()
window.title('鼠标连点器')
window.minsize(720,150)
window.maxsize(720,150)
tk.Label(window,text='每秒点击次数:',bg='#FFFFFF',activebackground='#FFFFFF',activeforeground='#0000FF').place(x=0,y=0,height=50,width=180)
tk.Label(window,text='几秒之后点击:',bg='#FFFFFF',activebackground='#FFFFFF',activeforeground='#0000FF').place(x=0,y=50,height=50,width=180)
tk.Label(window,text='要点击多少次:',bg='#FFFFFF',activebackground='#FFFFFF',activeforeground='#0000FF').place(x=0,y=100,height=50,width=180)
speed=tk.Entry(window)
speed.place(x=180,y=0,width=180,height=50)
timetoclick=tk.Entry(window)
timetoclick.place(x=180,y=50,width=180,height=50)
clicktime=tk.Entry(window)
clicktime.place(x=180,y=100,width=180,height=50)
click = [
    ('左键点击','left'), 
    ('中键点击','middle'),
    ('右键点击','right')]
clickmode = tk.StringVar()
tmp=0
def okclickmode():
    global click_
    click_=clickmode.get()
for name,mode in click:
    chooseclickmode = tk.Radiobutton(window,text = name, variable = clickmode,value =mode,font=('Arial',10),command=okclickmode,bg='#FFFFFF',activebackground='#FFFFFF',activeforeground='#0000FF')
    chooseclickmode.place(x=360,y=tmp,height=50,width=180)
    tmp+=50
def click123():
	speed_=1/int(speed.get())
	timetoclick_=int(timetoclick.get())
	clicktime_=int(clicktime.get())
	time.sleep(timetoclick_)
	for i in range(clicktime_):
		pyautogui.click(button=f'{click_}')
		time.sleep(speed_)
tk.Button(window,text='开始点击',command=click123,bg='#FFFFFF',activebackground='#FFFFFF',activeforeground='#0000FF').place(x=540,y=0,width=180,height=50)
def website():
    webbrowser.open_new_tab("https://github.com/x543054305/mouse-clicker")
tk.Button(window,text='程序主页',command=website,bg='#FFFFFF',activebackground='#FFFFFF',activeforeground='#0000FF').place(x=540,y=50,width=180,height=50)
def close():
    window.destroy()
tk.Button(window,text='退出程序',command=close,bg='#FFFFFF',activebackground='#FFFFFF',activeforeground='#0000FF').place(x=540,y=100,width=180,height=50)
window.mainloop()
