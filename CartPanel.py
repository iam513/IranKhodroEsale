from tkinter import *
from customtkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from SalePanel import *
import json


def setup_window():
    window = Tk()
    window.geometry("1166x718")
    window.resizable(False, False)
    window.title("EsaleCart")
    return window


def setup_TopFrame(window):
    TopFrame = Frame(window, height=50, bg="#122dc9")

    TopFrame.pack(side="top", fill="x")
    return TopFrame


def TopFrame_components(FrameToolbar: Frame, usernamevalue: str, window):
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
    Label(FrameToolbar, text="CART:", font=font_title, fg="white", bg="#122dc9").place(
        anchor="w", rely=0.5, relx=0.1
    )

    font_lbl_sign_in = CTkFont(family="impress", size=35)
    Label(
        FrameToolbar,
        text=usernamevalue,
        font=font_lbl_sign_in,
        fg="white",
        bg="#122dc9",
    ).place(anchor="w", rely=0.45, relx=0.18)

    # oon khat yazide
    ttk.Separator(FrameToolbar, orient="vertical").place(
        anchor="w", relx=0.33, rely=0.5, relheight=1
    )

    # button exit
    def goto_SellPanel(window):
        window.destroy()
        main_SalePanel()

    Button(
        FrameToolbar,
        text="Exit",
        font=("Arial", 24, "bold"),
        width=3,
        height=2,
        bg="#122dc9",
        border=False,
        cursor="hand2",
        fg="white",
        activebackground="red",
        command=lambda: goto_SellPanel(window),
    ).place(anchor="w", relx=0.534, rely=0.5)


def setup_DesFrame(window):
    FrameDes = Frame(window, height=600, bg="#636770")
    FrameDes.pack(fill="x")
    return FrameDes


all_frames = []


def DesFrame_components(usernamevalue, FrameDes: Frame):
    global all_frames
    with open("users.json", "r") as myfile:
        result = json.load(myfile)
        cars_dict = result[usernamevalue]["cars"]
    ColorFrames = "#8bbafc"
    Frame1 = Frame(FrameDes, height=150, bg=ColorFrames)
    Frame2 = Frame(FrameDes, height=150, bg=ColorFrames)
    Frame3 = Frame(FrameDes, height=150, bg=ColorFrames)
    Frame4 = Frame(FrameDes, height=150, bg=ColorFrames)

    Frame1.pack(fill="x")
    Frame2.pack(fill="x")
    Frame3.pack(fill="x")
    Frame4.pack(fill="x")

    all_frames.append(Frame1)
    all_frames.append(Frame2)
    all_frames.append(Frame3)
    all_frames.append(Frame4)

    car_names = cars_dict.keys()
    all_frames = all_frames[0 : len(car_names)]

    def pricecar(carname):
        if carname == "206":
            return 1000
        if carname == "405":
            return 2000
        if carname == "rana":
            return 3000
        if carname == "dena":
            return 4000

    for frame, carname in zip(all_frames, car_names):
        carnumber = cars_dict[carname]["num"]
        font_loading = CTkFont(family="Uni Sans Heavy CAPS", size=20)
        Label(frame, text=carname, bg=ColorFrames, font=font_loading).pack()
        imagestr = "images/" + carname + "cart" + ".jpg"
        myImage = Image.open(imagestr)
        photoBack = ImageTk.PhotoImage(myImage)
        bg_panel = Label(frame, text="", image=photoBack, bg=ColorFrames)
        bg_panel.image = photoBack
        bg_panel.pack(side="left", fill="y")
        carnumbertxt = "Numbers: " + str(carnumber)
        Label(frame, text=carnumbertxt, bg=ColorFrames, font=font_loading).pack()

        textprice = "Price: " + str(pricecar(carname) * carnumber)
        Label(frame, text=textprice, bg=ColorFrames, font=font_loading).pack()


def setup_TotalFrame(window):
    FrameTotal = Frame(window, height=68, bg="#6269bf")
    FrameTotal.pack(side="bottom", fill="x")
    return FrameTotal


def TotalFrame_components(FrameTotal: Frame, usernamevalue: str):

    with open("users.json", "r") as myfile:
        result = json.load(myfile)
        cars_dict = result[usernamevalue]["cars"]
        print(cars_dict)

    font_title = CTkFont(family="Uni Sans Heavy CAPS", size=30)
    Label(
        FrameTotal, text="Total Price:", font=font_title, fg="white", bg="#6269bf"
    ).place(x=30, y=15)

    def pricecar(cars):
        if cars == "206":
            return 1000
        if cars == "405":
            return 2000
        if cars == "rana":
            return 3000
        if cars == "dena":
            return 4000

    TotalPrice = 0
    for cars in cars_dict:
        num = cars_dict[cars]["num"]
        price = pricecar(cars)
        print(num)
        print(price)
        pricet = price * num
        TotalPrice = TotalPrice + pricet

    txtTotalPrice = str(TotalPrice)
    print(TotalPrice)
    Label(
        FrameTotal, text=txtTotalPrice, font=font_title, fg="white", bg="#6269bf"
    ).place(x=250, y=15)


def main_KartPanel(usernamevalue="shantia"):
    window = setup_window()
    FrameToolbar = setup_TopFrame(window)
    TopFrame_components(FrameToolbar, usernamevalue, window)
    FrameDes = setup_DesFrame(window)
    DesFrame_components(usernamevalue, FrameDes)
    FrameTotal = setup_TotalFrame(window)
    TotalFrame_components(FrameTotal, usernamevalue)

    window.mainloop()


if __name__ == "__main__":
    main_KartPanel()
