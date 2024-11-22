import random
import time
import string
from tkinter import *
from customtkinter import *
from PIL import ImageTk, Image
from loginPage import *


def window_stp():
    window = Tk()
    window.geometry("400x400")
    window.resizable(False, False)
    window.overrideredirect(True)
    height = 430
    width = 530
    x = window.winfo_screenwidth() // 2 - width // 2
    y = window.winfo_screenheight() // 2 - height // 2
    window.geometry(f"{width}x{height}+{x}+{y}")
    window.title("513")
    return window


def window_bg(window: Tk):
    myImage = Image.open("images/download.png")
    photoBack = ImageTk.PhotoImage(myImage)
    bg_panel = Label(window, text="", image=photoBack)
    bg_panel.image = photoBack
    bg_panel.pack()


def loading_component(window: Tk):

    font_loading = CTkFont(family="Uni Sans Heavy CAPS", size=20)

    lable1 = Label(window, text="MADE BY:", font=font_loading, bg="#708090")
    lable1.place(x=165, y=150)

    test = Label(window, text="salam", font=("Arial", 30, "bold"), bg="#708090")
    test.place(x=200, y=190)

    return test


result = ""


def animation(test: Label):

    global result
    letters = string.ascii_letters
    target = "SHANTIA"
    for i in target:
        while True:
            l = random.choice(letters)
            test.config(text=result + l)
            test.update()
            if l == i:
                result += l
                break
            time.sleep(0.001)

    time.sleep(1)
    for j in range(20):
        for color in ["red", "dark blue"]:
            test.configure(fg=color)
            test.update()
            time.sleep(0.01)


def main_loading():
    window = window_stp()
    window_bg(window)
    test = loading_component(window)
    animation(test)
    time.sleep(1.5)
    window.destroy()
    window.mainloop()
    main_login()


main_loading()
