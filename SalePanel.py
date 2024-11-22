from tkinter import *
from customtkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import CartPanel
import json


def window_setup():
    window = Tk()
    window.resizable(False, False)
    height = 718
    width = 1166
    x = window.winfo_screenwidth() // 2 - width // 2
    y = window.winfo_screenheight() // 2 - height // 2
    window.geometry(f"{width}x{height}+{x}+{y}")
    return window


def set_FrameToolbar(window: Tk):
    FrameToolbar = Frame(window, height=50, bg="#122dc9")

    FrameToolbar.pack(side="top", fill="x")
    return FrameToolbar


def toolbar_components(FrameToolbar: Frame, usernamevalue: str, window: Tk):
    # profile pic
    myimage = Image.open("images/LogoSignIn.png")
    photoBack = ImageTk.PhotoImage(myimage)
    side_image = Label(
        FrameToolbar, text="", image=photoBack, bg="#122dc9", height=60, width=100
    )
    side_image.image = photoBack
    side_image.place(anchor="w", rely=0.4)

    # Welcome text
    font_title = CTkFont(family="Uni Sans Heavy CAPS", size=30)
    Label(
        FrameToolbar, text="WELCOME", font=font_title, fg="white", bg="#122dc9"
    ).place(anchor="w", rely=0.5, relx=0.1)

    font_lbl_sign_in = CTkFont(family="impress", size=35)
    Label(
        FrameToolbar,
        text=usernamevalue,
        font=font_lbl_sign_in,
        fg="white",
        bg="#122dc9",
    ).place(anchor="w", rely=0.45, relx=0.23)

    # oon khat yazide
    ttk.Separator(FrameToolbar, orient="vertical").place(
        anchor="w", relx=0.33, rely=0.5, relheight=1
    )

    # kart button
    def gotoKart(usernamevalue, window: Tk):
        window.destroy()
        CartPanel.main_KartPanel(usernamevalue)

    Button(
        FrameToolbar,
        text="🛒",
        font=("Arial", 30, "bold"),
        # image=photoBack2,
        width=2,
        height=2,
        bg="#122dc9",
        border=False,
        cursor="hand2",
        fg="white",
        activebackground="#0e239e",
        command=lambda: gotoKart(usernamevalue, window),
    ).place(anchor="w", relx=0.334, rely=0.5)


def set_frameSellList(window: Tk):
    FrameSellList = Frame(window, width=1166, height=50, bg="#483c32")
    FrameSellList.pack(side="top", fill="both", expand=True)
    return FrameSellList


def FrameSellList_components(FrameSellList: Frame, usernamevalue: str):
    imagepeju206 = Image.open("images/206.png")
    photoBack4 = ImageTk.PhotoImage(imagepeju206)
    peju206 = Label(FrameSellList, width=500, height=250, text="", image=photoBack4)
    peju206.image = photoBack4
    peju206.place(x=20, y=30)

    imagepeju405 = Image.open("images/405.png")
    photoBack5 = ImageTk.PhotoImage(imagepeju405)
    peju405 = Label(FrameSellList, width=500, height=250, bg="orange", image=photoBack5)
    peju405.image = photoBack5
    peju405.place(x=650, y=30)

    imageDena = Image.open("images/dena.png")
    photoBack6 = ImageTk.PhotoImage(imageDena)
    Dena = Label(FrameSellList, width=500, height=250, bg="orange", image=photoBack6)
    Dena.image = photoBack6
    Dena.place(x=20, y=350)

    imageRana = Image.open("images/rana.png")
    photoBack7 = ImageTk.PhotoImage(imageRana)
    Rana = Label(FrameSellList, width=500, height=250, bg="orange", image=photoBack7)
    Rana.image = photoBack7
    Rana.place(x=650, y=350)

    # .place(x=650, y=350)

    # buttons
    def forfun(usernamevalue: str, CarValue: str):
        with open("users.json", "r") as myfile:
            result = json.load(myfile)
            cars_dict = result[usernamevalue]["cars"]
            car_lst = []
            for CarName in cars_dict:
                car_lst.append(CarName)
                if CarName == CarValue:
                    num = cars_dict[CarValue]["num"]
                    num = num + 1
                    cars_dict[CarValue].update({"num": num})
                    with open("users.json", "w") as myfile:
                        json.dump(result, myfile)
            if CarValue not in car_lst:
                cars_dict.update({CarValue: {"num": 1}})
                with open("users.json", "w") as myfile:
                    json.dump(result, myfile)

    font_buy = CTkFont(family="impress", size=16)
    Button(
        FrameSellList,
        text="ADD TO CART",
        font=font_buy,
        bg="#122dc9",
        # border=False,
        cursor="hand2",
        fg="white",
        activebackground="green",
        width=15,
        height=1,
        command=lambda: forfun(usernamevalue, "206"),
    ).place(x=200, y=290)

    Button(
        FrameSellList,
        text="ADD TO CART",
        font=font_buy,
        bg="#122dc9",
        # border=False,
        cursor="hand2",
        fg="white",
        activebackground="green",
        width=15,
        height=1,
        command=lambda: forfun(usernamevalue, "405"),
    ).place(x=830, y=290)

    Button(
        FrameSellList,
        text="ADD TO CART",
        font=font_buy,
        bg="#122dc9",
        # border=False,
        cursor="hand2",
        fg="white",
        activebackground="green",
        width=15,
        height=1,
        command=lambda: forfun(usernamevalue, "dena"),
    ).place(x=200, y=610)

    Button(
        FrameSellList,
        text="ADD TO CART",
        font=font_buy,
        bg="#122dc9",
        # border=False,
        cursor="hand2",
        fg="white",
        activebackground="green",
        width=15,
        height=1,
        command=lambda: forfun(usernamevalue, "rana"),
    ).place(x=830, y=610)


def main_SalePanel(usernamevalue="shantia"):
    window = window_setup()
    FrameToolbar = set_FrameToolbar(window)
    toolbar_components(FrameToolbar, usernamevalue, window)
    FrameSellList = set_frameSellList(window)
    FrameSellList_components(FrameSellList, usernamevalue)

    window.mainloop()


if __name__ == "__main__":
    main_SalePanel()
