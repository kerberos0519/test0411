from tkinter import *
from PIL import Image, ImageTk


price = 0
money = 0
window = Tk()
window.title("자판기")
window.geometry('1200x600')

#태홍이가 이미지 첨부가능하게 함
image1 = Image.open("D:\\0411 day\\test0411-1\\americano.jpg")
image1 = image1.resize((180, 180), Image.ANTIALIAS)
photo1 = ImageTk.PhotoImage(image1)
label1 = Label(window, image=photo1)
label1.place(x=200, y=300)

image2 = Image.open("D:\\0411 day\\test0411-1\\icecho.jpg")
image2 = image2.resize((180, 180), Image.ANTIALIAS)
photo2 = ImageTk.PhotoImage(image2)
label2 = Label(window, image=photo2)
label2.place(x=200, y=400)

image3 = Image.open("D:\\0411 day\\test0411-1\\mix.jpg")
image3 = image3.resize((180, 180), Image.ANTIALIAS)
photo3 = ImageTk.PhotoImage(image3)
label3 = Label(window, image=photo3)
label3.place(x=200, y=500)

image4 = Image.open("D:\\0411 day\\test0411-1\\cafe.jpg")
image4 = image4.resize((180, 180), Image.ANTIALIAS)
photo4 = ImageTk.PhotoImage(image4)
label4 = Label(window, image=photo4)
label4.place(x=300, y=400)

image5 = Image.open("D:\\0411 day\\test0411-1\\icecho.jpg")
image5 = image5.resize((180, 180), Image.ANTIALIAS)
photo5 = ImageTk.PhotoImage(image5)
label5= Label(window, image=photo5)
label5.place(x=300, y=500)

image6 = Image.open("D:\\0411 day\\test0411-1\\ice tea.jpg")
image6 = image6.resize((180, 180), Image.ANTIALIAS)
photo6 = ImageTk.PhotoImage(image6)
label6 = Label(window, image=photo6)
label6.place(x=300, y=600)




frame = Frame(window)
frame.pack(side=RIGHT, padx=10, pady=50)

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

# 아메리카노 버튼 클릭 시 호출되는 함수
def p_americano():
    global price
    if inventory["americano"] > 0:
        price=1800
        inventory["americano"] -= 1
        process()
        update_inventory_labels()
    else:
        en2.insert(0, "품절")

# 믹스커피 버튼 클릭 시 호출되는 함수
def p_mix():
    global price
    if inventory["mix"] > 0:
        price=300
        inventory["mix"] -= 1
        process()
        update_inventory_labels()
    else:
        en2.insert(0, "품절")

# 아이스초코 버튼 클릭 시 호출되는 함수
def p_icechoco():
    global price
    if inventory["icechoco"] > 0:
        price=2800
        inventory["icechoco"] -= 1
        process()
        update_inventory_labels()
    else:
        en2.insert(0, "품절")

# 에스프레소 버튼 클릭 시 호출되는 함수
def p_espresso():
    global price
    if inventory["espresso"] > 0:
        price=3800
        inventory["espresso"] -= 1
        process()
        update_inventory_labels()
    else:
        en2.insert(0, "품절")

# 카페라떼 버튼 클릭 시 호출되는 함수
def p_latte():
    global price
    if inventory["latte"] > 0:
        price=2500
        inventory["latte"] -= 1
        process()
        update_inventory_labels()
    else:
        en2.insert(0, "품절")

# 아이스티 버튼 클릭 시 호출되는 함수
def p_lemonade():
    global price
    if inventory["lemonade"] > 0:
        price=2300
        inventory["lemonade"] -= 1
        process()
        update_inventory_labels()
    else:
        en2.insert(0, "품절")

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
la1.pack(side="bottom", padx=8, pady=8)
en1 = Entry(window)
en1.pack(side="bottom", padx=8, pady=8)

la2 = Label(window,text="거스름돈")
la2.pack(side="bottom", padx=5, pady=5)
en2 = Entry(window)
en2.pack(side="bottom", padx=5, pady=5)

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
bt6.place(x=300, y=250)

# 음료수 수량 정보를 저장하는 딕셔너리
inventory = {"americano": 10, "mix": 10, "icechoco": 10, "latte": 10, "espresso": 10, "lemonade": 10}

# 아메리카노 버튼 클릭 시 호출되는 함수
def p_americano():
    global price
    if inventory["americano"] > 0:
        price=1800
        inventory["americano"] -= 1
        process()
        update_inventory_labels()
    else:
        en2.insert(0, "품절")
        

# 레이블 업데이트 함수
def update_inventory_labels():
    la3.config(text="아메리카노: " + str(inventory["americano"]))
    la4.config(text="믹스커피: " + str(inventory["mix"]))
    la5.config(text="아이스초코: " + str(inventory["icechoco"]))
    la6.config(text="카페라떼: " + str(inventory["latte"]))
    la7.config(text="에스프레소: " + str(inventory["espresso"]))
    la8.config(text="아이스티: " + str(inventory["lemonade"]))

# 아메리카노 수량 레이블
la3 = Label(window, text="아메리카노: " + str(inventory["americano"]))
la3.place(x=600, y=50)

# 믹스커피 수량 레이블
la4 = Label(window, text="믹스커피: " + str(inventory["mix"]))
la4.place(x=600, y=100)

# 아이스초코 수량 레이블
la5 = Label(window, text="아이스초코: " + str(inventory["icechoco"]))
la5.place(x=600, y=150)

# 에스프레소 수량 레이블
la6 = Label(window, text="에스프레소: " + str(inventory["espresso"]))
la6.place(x=600, y=200)

# 카페라떼 수량 레이블
la7 = Label(window, text="카페라떼: " + str(inventory["latte"]))
la7.place(x=600, y=250)

# 아이스티 수량 레이블
la8 = Label(window, text="아이스티: " + str(inventory["lemonade"]))
la8.place(x=600, y=300)

window.mainloop()
