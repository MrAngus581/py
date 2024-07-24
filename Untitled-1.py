import tkinter as tk
from tkinter.constants import *
from tkinter import ttk
import webbrowser
import os
import openpyxl



window = tk.Tk()
window.title("教師成績登記系統(需放大使用)")
window.minsize(width=1800, height=900)
window.resizable(width=True, height=True)
label = tk.Label(window,
                  text='請登入',
                  font=('Arial',40,'bold'),
                  fg='blue')
label.pack(side='top', padx=20, pady=20)

f = open('帳號密碼.txt')
line = f.readline().replace('\n',"") #去掉換行
line2 = f.readline().replace('\n',"") #去掉換行
f.close()






text1 =  tk.Text(window, width=60, height=1.4, borderwidth=3, wrap="none", font=("bold",20))
text1.pack(side="bottom",padx=0, pady=10)




text2 =  tk.Text(window, width=60, height=1.4, borderwidth=3, wrap="none", font=("bold",20), )
text2.pack(side="bottom")





label_user = tk.Label(window,
                      text="帳號",
                      font=('bold',20),
                      fg="black")
label_user.place(y=900)
label_user.pack(side="bottom",after=text2)

label_password = tk.Label(window,
                      text="密碼",
                      font=('bold',20),
                      fg="black")
label_password.pack(side="bottom",after=text1)

label_bg = tk.Label(background="gray",height=100,width=100)
label_bg.place(y=0)
label_bg.lift()
label_bg.pack(fill="both")
quit_pages =tk.Button(text="退出",height=0,width=0,font=('Arial',30,'bold'),command=window.quit)
quit_pages.pack()
quit_pages.place(x=0,y=940)


    



def send_sign():
    label.pack_forget()
    label_user.pack_forget()
    label_password.pack_forget()
    text1.pack_forget()
    text2.pack_forget()
    sign_clean.destroy()
    sign_in.destroy()
    label_main_t.pack()
    label_main_t.place(x=890,y=0)
    tool_select.pack()
    tool_select.place(y=800)
    tool_select_check.pack()
    tool_select_check.place(x=50,y=820)
    tool_select_t.pack()
    tool_select_t.place(y=770)
    object_ch.pack()
    object_ch.place(y=80)
    object_en.pack()
    object_en.place(y=110)
    object_ma.pack()
    object_ma.place(y=140)
    object_gr.pack()
    object_gr.place(y=170)
    object_hi.pack()
    object_hi.place(y=200)
    object_ci.pack()
    object_ci.place(y=230)
    object_bi.pack()
    object_bi.place(y=260)
    object_PhCh.pack()
    object_PhCh.place(y=290)
    object_ge.pack()
    object_ge.place(y=320)
    object_PE.pack()
    object_PE.place(y=350)
    object_art.pack()
    object_art.place(y=380)
    object_t.pack()
    object_t.place(x=0,y=0)
    bs.pack()
    bs.place(x=0,y=0)
    announcement.pack(padx=30,pady=30)
    announcement.place(x=650,y=400)
    scrollbar_frame.pack()
    scrollbar_frame.place(x=650,y=400)
    frame_text.pack()
    announcement_tittle.pack()
    announcement_tittle.place(x=900,y=700)


def get():
    get_a = text2.get("0.0","end")
    get_p = text1.get("0.0","end")
    get_ar = get_a.replace('\n',"")
    get_pr = get_p.replace('\n',"")
    if line == get_ar:
        check1 = "o"
    
    if line2 == get_pr:
        check2 = "k"

    if check1+check2 == "ok":
        sign_in.configure(command=send_sign)
    






sign_in = tk.Button(text="登入",font=('Arial',10,'bold'),command=get)
sign_in.pack()
sign_in.place(x=1360,y=890)


def clear_text():
    text1.delete("1.0","end")
    text2.delete("1.0","end")

sign_clean = tk.Button(text="清除",font=('Arial',10,'bold'),command=clear_text)                                                  #need command!!!!!!!!!!
sign_clean.pack()
sign_clean.place(x=1360,y=970)

label_main_t = tk.Label(text="歡迎回來!",bg="gray",font=("Arial",30,"bold"),fg="white")
quit_pages.lift()

tool_select = ttk.Combobox(window,values=['計算機','放大鏡','開啟google',"開啟學校網頁","開發人員"],height=9)

def open_tools():
    if tool_select.get() == "計算機":    
        cl_url = "https://www.google.com/search?q=%E8%A8%88%E7%AE%97%E6%A9%9F&oq=%E8%A8%88%E7%AE%97&gs_lcrp=EgZjaHJvbWUqDQgBEAAYgwEYsQMYgAQyDggAEEUYORhDGIAEGIoFMg0IARAAGIMBGLEDGIAEMgwIAhAAGEMYgAQYigUyDAgDEAAYQxiABBiKBTIMCAQQABhDGIAEGIoFMgwIBRAAGEMYgAQYigUyDAgGEAAYQxiABBiKBTIKCAcQABixAxiABDIMCAgQABhDGIAEGIoFMg8ICRAAGEMYsQMYgAQYigXSAQk3MzY0ajBqMTWoAgiwAgE&sourceid=chrome&ie=UTF-8" # 注意:"http://"不可省略
        webbrowser.open(cl_url)
    if tool_select.get() == "放大鏡":
        os_print = os.system("magnify")
        print(os_print)
    if tool_select.get() == "開啟google":
        g_url = "https://www.google.com"
        webbrowser.open(g_url)
    if tool_select.get() == "開啟學校網頁":
        ex_url = "https://www.tcjhs.tyc.edu.tw/"
        webbrowser.open(ex_url)
    if tool_select.get() == "開發人員":
        wr_url = "https://docs.google.com/document/d/1DMvGFlXtLo3I0Tu0Pu3nxEP0WJoEOm04Pq-QIwBEnJY/edit?usp=sharing"
        webbrowser.open(wr_url)

def send_s():
    s_url = "https://docs.google.com/document/d/1iaTy4pIi7C2g1Da6nnfQqbg-dnPgOqX32QE3Njkz8gQ/edit"
    webbrowser.open(s_url)
bs = tk.Button(text="",font=('Arial',1,'bold'),command=send_s,pady=400)

tool_select_check = tk.Button(text="開啟",font=("Arial",10,"bold"),command=open_tools)

tool_select_t = tk.Label(text="小小工具",bg="gray",fg="black",font=("Arial",13,"bold"),padx=32)

object_t = tk.Label(text="登記科目",bg="gray",fg="black",font=("Arial",13,"bold"),padx=2,pady=55)

def end():
    end_url = "https://docs.google.com/document/d/1s87vgDs08BeP-LfvbpFgZaEzawzI_Jwx6uJbUI5FvfU/edit"
    webbrowser.open(end_url)

object_ch = tk.Button(text="🅧",fg="black",font=("Arial",10,"bold"),width=10,command=None)
object_en = tk.Button(text="🅧",fg="black",font=("Arial",10,"bold"),width=10,command=None)
object_ma = tk.Button(text="🅧",fg="black",font=("Arial",10,"bold"),width=10,command=None)
object_gr = tk.Button(text="🅧",fg="black",font=("Arial",10,"bold"),width=10,command=None)
object_hi = tk.Button(text="🅧",fg="black",font=("Arial",10,"bold"),width=10,command=None)
object_ci = tk.Button(text="🅧",fg="black",font=("Arial",10,"bold"),width=10,command=None)
object_bi =tk.Button(text="🅧",fg="black",font=("Arial",10,"bold"),width=10,command=None)
object_PhCh = tk.Button(text="理化",fg="black",font=("Arial",10,"bold"),width=10,command=end)
object_ge = tk.Button(text="🅧",fg="black",font=("Arial",10,"bold"),width=10,command=None)
object_PE = tk.Button(text="🅧",fg="black",font=("Arial",10,"bold"),width=10,command=None)
object_art = tk.Button(text="🅧",fg="black",font=("Arial",10,"bold"),width=10,command=None)


scrollbar_frame = tk.Frame(window,height=16,width=61)
announcement = tk.Scrollbar(scrollbar_frame)

announcement_text = tk.StringVar()
announcement_text.set(("2024-7-12           系統上線","2024-7-14            系統更新")) #TAB*3
# 在 Frame 中加入 Listbox 元件，設定 yscrollcommand=scrollbar.set
listbox = tk.Listbox(scrollbar_frame,  listvariable=announcement_text, height=15, width=60, font=("Arial",15,"bold"),yscrollcommand=announcement.set)
listbox.pack(side='left', fill='y')    # 設定 Listbox 的位置以及填滿方式
announcement.config(command = listbox.yview)

announcement_tittle = tk.Label(text="lasdaksdk",font=("Arial",30,"bold"))


window.mainloop()



