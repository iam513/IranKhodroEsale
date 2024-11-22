from tkinter import *
from customtkinter import *
from tkextrafont import Font
import signupPage
from login_backend import *
from PIL import Image, ImageTk


def setup_window():
    window = Tk()
    window.geometry("1166x718")
    window.resizable(False, False)
    window.title("Management Budget")
    return window


def setup_background(window: Tk):
    myImage = Image.open("images/irankhodro.jpg")
    photoBack = ImageTk.PhotoImage(myImage)
    bg_panel = Label(window, text="", image=photoBack)
    bg_panel.image = photoBack  # save binary data
    bg_panel.pack()


def go_to_signup_module(window: Tk):
    window.destroy()
    signupPage.main_signup()


def setFrameLogin(window: Tk):
    LoginFrame = Frame(window, width=950, height=600, bg="#2e2929")
    LoginFrame.place(anchor="center", relx=0.5, rely=0.5)
    return LoginFrame


def loginComponent(LoginFrame: Frame, window: Tk):
    # heading
    font_title = CTkFont(family="Uni Sans Heavy CAPS", size=30)
    # font_title = Font(
    #     file="fonts/UniSansHeavy.otf", family="Uni Sans Heavy CAPS", size=30
    # )
    Label(
        LoginFrame, text="IRAN KHODRO ESALE", font=font_title, fg="white", bg="#2e2929"
    ).place(x=80, y=100)

    # open Photo
    myimage = Image.open("images/irankhodrologo.png")
    myimage = myimage.resize(size=(300, 300))
    photoBack2 = ImageTk.PhotoImage(myimage)
    side_image = Label(LoginFrame, text="", image=photoBack2, bg="#2e2929")
    side_image.image = photoBack2
    side_image.place(x=70, y=200)

    # Sign In Image
    myimage2 = Image.open("images/LogoSignIn.png")
    photoBack3 = ImageTk.PhotoImage(myimage2)
    side_image2 = Label(LoginFrame, text="", image=photoBack3, bg="#2e2929")
    side_image2.image = photoBack3
    side_image2.place(x=620, y=70)

    # Sign In Label
    font_lbl_sign_in = CTkFont(family="Dancing Script", size=16)

    Label(
        LoginFrame, text="Sign In", bg="#2e2929", fg="white", font=font_lbl_sign_in
    ).place(x=650, y=180)

    # userName
    userNameLabel = Label(
        LoginFrame,
        text="UserName",
        bg="#2e2929",
        fg="white",
        font=("Arial", 13, "bold"),
    )
    userNameLabel.place(x=550, y=300)

    username_entry = Entry(
        LoginFrame, bg="#2e2929", border=False, fg="white", font=("Arial", 15)
    )
    username_entry.place(x=580, y=335)
    Canvas(LoginFrame, width=350, height=1, highlightthickness=0, bg="#7c7d7c").place(
        x=550, y=360
    )

    myimage3 = Image.open("images/username_icon.png")
    photoBack4 = ImageTk.PhotoImage(myimage3)
    side_image3 = Label(LoginFrame, text="", image=photoBack4, bg="#2e2929")
    side_image3.image = photoBack4
    side_image3.place(x=550, y=333)

    # Password
    PasswordLabel = Label(
        LoginFrame,
        text="Password",
        bg="#2e2929",
        fg="white",
        font=("Arial", 13, "bold"),
    )
    PasswordLabel.place(x=550, y=380)
    Password_entry = Entry(
        LoginFrame, bg="#2e2929", border=False, fg="white", font=("Arial", 15)
    )
    Password_entry.place(x=580, y=415)
    Canvas(LoginFrame, width=350, height=1, highlightthickness=0, bg="#7c7d7c").place(
        x=550, y=440
    )

    myimage4 = Image.open("images/password_icon.png")
    photoBack5 = ImageTk.PhotoImage(myimage4)
    side_image4 = Label(LoginFrame, text="", image=photoBack5, bg="#2e2929")
    side_image4.image = photoBack5
    side_image4.place(x=550, y=412)

    # Login btn
    myimage5 = Image.open("images/btn1.png")
    myimage5 = myimage5.resize(size=(200, 40))
    photoBack6 = ImageTk.PhotoImage(myimage5)
    side_image5 = Button(
        LoginFrame,
        text="",
        image=photoBack6,
        bg="#2e2929",
        border=False,
        cursor="hand2",
        fg="white",
        activebackground="#2e2929",
        command=lambda: check_exist_user(username_entry, Password_entry, window),
    )
    Label(
        LoginFrame, text="Login", bg="#3047FF", fg="white", font=("Arial", 13, "bold")
    ).place(x=695, y=470)
    side_image5.image = photoBack6
    side_image5.place(x=620, y=460)

    # forget Password
    # Button(LoginFrame, text="forget password ?", border=False, bg="#696262", fg="white").place(x=620,y=480)

    # Sign Up btn
    sign_up_label = Label(
        LoginFrame,
        text="No account yet ?",
        font=("Arial", 11, "bold"),
        bg="#2e2929",
        fg="white",
    )
    sign_up_label.place(x=550, y=510)

    myimage6 = Image.open("images/register.png")
    photoBack7 = ImageTk.PhotoImage(myimage6)
    side_image6 = Button(
        LoginFrame,
        text="",
        image=photoBack7,
        bg="#2e2929",
        border=False,
        activebackground="#2e2929",
        command=lambda: go_to_signup_module(window),
    )
    side_image6.image = photoBack7
    side_image6.place(x=540, y=535)


def main_login():
    window = setup_window()
    setup_background(window)
    LoginFrame = setFrameLogin(window)
    loginComponent(LoginFrame, window)
    window.mainloop()


if __name__ == "__main__":
    main_login()
