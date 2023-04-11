
from tkinter import *
import tkinter
from PIL import Image, ImageTk


price = 0
money = 0
window = Tk()
window.title("자판기")
window.geometry('500x300+200+200')


def process():
    global money

    en1.delete(0,"end")
    en2.delete(0,"end")

    if money< 100 :
        en2.insert(0,str("잔액이 부족합니다."))
    elif money<200 and price==200:
        en2.insert(0,str("믹스커피만 가능합니다"))

    else :
        money -= price
        en2.insert(0,str(money))

def p_americano():
    global price
    price=200
    process()
    

    image = Image.open("D:/dategit/img/americano.png")
    size = (300, 300)
    image.thumbnail(size, Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    label = tkinter.Label(window, image=photo)
    label.image = photo
    label.place(x=200, y=50)
    

def p_mix():
    global price
    price=100
    process()
    

    image = Image.open("D:/dategit/img/mix2.jpg")
    size = (250, 250)
    image.thumbnail(size, Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    label = tkinter.Label(window, image=photo)
    label.image = photo
    label.place(x=200, y=50)
    

def p_icechoco():
    global price
    price=150
    process()
    
    
    image = Image.open("D:/dategit/img/icechoco.png")
    size = (300, 300)
    image.thumbnail(size, Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    label = tkinter.Label(window, image=photo)
    label.image = photo
    label.place(x=200, y=50)
    
    
def p_milktea():
    global price
    price=300
    process()
    
    
    image = Image.open("D:/dategit/img/milktea2.jpg")
    size = (250, 250)
    image.thumbnail(size, Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    label = tkinter.Label(window, image=photo)
    label.image = photo
    label.place(x=200, y=50)
    

def p_get():
    global money
    remoney = int(en1.get())
  
    if money>0 :
        money += remoney
        en1.delete(0,"end")
        en2.delete(0,"end")
        en2.insert(0,str(money))

    else :
        money = remoney
        en2.delete(0,"end")
        en,insert(0,str("커피를 선택하세요."))

la1 = Label(window,text="투입금액")
la1.grid(row=0, column=0)
en1 = Entry(window)
en1.grid(row=0, column=1)

la2 = Label(window,text="거스름돈")
la2.grid(row=1, column=0)
en2 = Entry(window)
en2.grid(row=1, column=1)

bt1 = Button(window,height='2',width='20',text="아메리카노 200원", command=p_americano)
bt1.place(x=50, y=50)
bt2 = Button(window,height='2',width='20',text="믹스커피 100원", command=p_mix)
bt2.place(x=50, y=100)
bt3 = Button(window,height='2',width='20',text="아이스초코 150원", command=p_icechoco)
bt3.place(x=50, y=150)
bt4 = Button(window,height='2',width='20',text="밀크티 500원", command=p_milktea)
bt4.place(x=50, y=200)

bt5 = Button(window, text="확인", command=p_get)
bt5.grid(row=0, column=3)



window.mainloop()