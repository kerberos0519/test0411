# import tkinter as tk
# from PIL import Image, ImageTk

# # 윈도우 생성
# root = tk.Tk()

# # 이미지 불러오기
# image = Image.open("D:/dategit/img/americano.png")
# photo = ImageTk.PhotoImage(image)

# # 이미지 보여줄 라벨 생성
# label = tk.Label(root, image=photo)
# label.pack()

# # 버튼 생성
# button = tk.Button(root, text="이미지 보기", command=lambda: label.config(image=photo))
# button.pack()

# # 윈도우 실행
# root.mainloop()










# import tkinter as tk
# from PIL import Image, ImageTk

# # 윈도우 생성
# root = tk.Tk()

# # 이미지 불러오기
# image = Image.open("D:/dategit/img/americano.png")
# resized_image = image.resize((10, 10)) 
# photo = ImageTk.PhotoImage(image)

# # 이미지 보여줄 라벨 생성
# label = tk.Label(root)
# label.pack()

# # 버튼 생성
# button = tk.Button(root, text="이미지 보기", command=lambda: label.config(image=photo))
# button.pack()

# # 초기에는 이미지를 보이지 않도록 설정
# label.config(image=None)

# # 윈도우 실행
# root.mainloop()










def process():
    global money

    en1.delete(0,"end")
    en2.delete(0,"end")

    if money < 100 :
        en2.insert(0, "잔액이 부족합니다.")
    elif money < 200 and price == 200:
        en2.insert(0, "믹스커피만 가능합니다")
    else:
        money -= price
        en2.insert(0, str(money))
        
        # 이미지 불러오기 및 크기 조절
        image = Image.open("image.png")
        resized_image = image.resize((100, 100))
        photo = ImageTk.PhotoImage(resized_image)
        
        # 이미지 보여줄 라벨 생성
        label = Label(window, image=photo)
        label.image = photo  # 참조를 유지하기 위해 변수에 할당
        
        # 라벨 위치 조정
        label.place(x=200, y=100)