
from tkinter import *
import tkinter


price = 0
money = 0
window = Tk()
window.title("자판기")
window.geometry('700x500')

#im=tkinter.Label(window,image=image)
#im.pack()

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
    price=1800
    process()

def p_mix():
    global price
    price=300
    process()

def p_icechoco():
    global price
    price=2800
    process()

def p_lemonade():
    global price
    price=2300
    process()

def p_latte():
    global price
    price=2500
    process()

def p_espresso():
    global price
    price=3800
    process()

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

#선민이가 작업했음 4-11 10시55분
bt1 = Button(window,height='3',width='30',text="아메리카노 1800원", command=p_americano)
bt1.place(x=50, y=50)
bt2 = Button(window,height='3',width='30',text="믹스커피 300원", command=p_mix)
bt2.place(x=50, y=150)
bt3 = Button(window,height='3',width='30',text="아이스초코 2800원", command=p_icechoco)
bt3.place(x=50, y=250)
bt4 = Button(window,height='3',width='30',text="에스프레소 3800원", command=p_espresso)
bt4.place(x=300, y=50)
bt5 = Button(window, height='3', width='30', text="카페라떼 2500원", command=p_latte)
bt5.place(x=300, y=150)
bt6 = Button(window, height='3', width='30', text="아이스티 2300원", command=p_lemonade)
bt6.place(x=300, y=250)
bt6 = Button(window, text="확인", command=p_get)
bt6.grid(row=0, column=3)

window.mainloop()
