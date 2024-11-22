from tkinter import *
from PIL import Image, ImageTk
from tkextrafont import Font
from signup_backend import *
from customtkinter import *

# # from loginPage import *
# from loginPage import *
import loginPage


def setup_windowSignUp2():
    window = Tk()
    window.geometry("1166x718")
    window.resizable(False, False)
    window.title("Sign Up Budget Management")
    return window


def setup_background2(window: Tk):
    myImage = Image.open("images/signupbg.png")
    photoBack = ImageTk.PhotoImage(myImage)
    bg_panel = Label(window, text="", image=photoBack)
    bg_panel.image = photoBack  # save binary data
    bg_panel.pack()


def go_to_signin_module(window: Tk):
    window.destroy()
    loginPage.main_login()


def setFramSignUp(window: Tk):
    signupFrame = Frame(window, width=950, height=600, bg="#2e2929")
    signupFrame.place(anchor="center", relx=0.5, rely=0.5)
    return signupFrame


def signupComponent(signupFrame: Frame, window: Tk, username_value):
    # heading

    back_btn = Button(
        signupFrame,
        text="← Back",
        fg="white",
        command=lambda: go_to_signin_module(window),
        bg="#2e2929",
        border=False,
        font=("Arial", 10, "bold"),
    )
    back_btn.place(x=5, y=5)

    font_title = CTkFont(family="Uni Sans Heavy CAPS", size=30)
    # font_title = Font(
    #     file="fonts/UniSansHeavy.otf", family="Uni Sans Heavy CAPS", size=30
    # )
    Label(
        signupFrame, text="Create an account", font=font_title, fg="white", bg="#2e2929"
    ).place(x=100, y=60)

    # open Photo
    myimage = Image.open("images/SignupIcon.png")
    # myimage = myimage.resize(size=(400, 400))
    photoBack2 = ImageTk.PhotoImage(myimage)
    side_image = Label(signupFrame, text="", image=photoBack2, bg="#2e2929")
    side_image.image = photoBack2
    side_image.place(x=5, y=140)

    # Sign Up Image
    myimage2 = Image.open("images/profile.png")
    photoBack3 = ImageTk.PhotoImage(myimage2)
    side_image2 = Label(signupFrame, text="", image=photoBack3, bg="#2e2929")
    side_image2.image = photoBack3
    side_image2.place(x=650, y=80)

    # Sign Up Label
    font_lbl_sign_in = CTkFont(family="Dancing Script", size=16)
    # font_lbl_sign_in = Font(
    #     file="fonts/DancingScript.ttf", family="Dancing Script", weight="bold", size=16
    # )
    Label(
        signupFrame, text="Sign Up", bg="#2e2929", fg="white", font=font_lbl_sign_in
    ).place(x=660, y=180)

    # error label
    error_lbl = Label(
        signupFrame, text="", bg="#2e2929", fg="#ed1515", font=("Arial", 13, "bold")
    )
    error_lbl.place(x=605, y=250)

    # userName
    userNameLabel = Label(
        signupFrame,
        text="UserName",
        bg="#2e2929",
        fg="white",
        font=("Arial", 13, "bold"),
    )
    userNameLabel.place(x=550, y=300)

    default = StringVar()
    if username_value != None:
        default.set(username_value)

    username_entry = Entry(
        signupFrame,
        bg="#2e2929",
        border=False,
        fg="white",
        font=("Arial", 15),
        textvariable=default,
    )
    username_entry.place(x=580, y=335)
    Canvas(signupFrame, width=350, height=1, highlightthickness=0, bg="#7c7d7c").place(
        x=550, y=360
    )

    myimage3 = Image.open("images/username_icon.png")
    photoBack4 = ImageTk.PhotoImage(myimage3)
    side_image3 = Label(signupFrame, text="", image=photoBack4, bg="#2e2929")
    side_image3.image = photoBack4
    side_image3.place(x=550, y=333)

    # Password
    PasswordLabel = Label(
        signupFrame,
        text="Password",
        bg="#2e2929",
        fg="white",
        font=("Arial", 13, "bold"),
    )
    PasswordLabel.place(x=550, y=380)

    Password_entry = Entry(
        signupFrame,
        bg="#2e2929",
        border=False,
        show="*",
        fg="white",
        font=("Arial", 15),
    )
    Password_entry.place(x=580, y=415)
    Canvas(signupFrame, width=350, height=1, highlightthickness=0, bg="#7c7d7c").place(
        x=550, y=440
    )

    myimage4 = Image.open("images/password_icon.png")
    photoBack5 = ImageTk.PhotoImage(myimage4)
    side_image4 = Label(signupFrame, text="", image=photoBack5, bg="#2e2929")
    side_image4.image = photoBack5
    side_image4.place(x=550, y=412)

    # signUp btn
    myimage5 = Image.open("images/btn1.png")
    myimage5 = myimage5.resize(size=(200, 40))
    photoBack6 = ImageTk.PhotoImage(myimage5)
    side_image5 = Button(
        signupFrame,
        text="",
        image=photoBack6,
        bg="#2e2929",
        border=False,
        cursor="hand2",
        fg="white",
        activebackground="#2e2929",
        command=lambda: authentication_user(username_entry, Password_entry, error_lbl),
    )
    Label(
        signupFrame,
        text="Sign Up",
        bg="#3047FF",
        fg="white",
        font=("Arial", 13, "bold"),
    ).place(x=695, y=470)
    side_image5.image = photoBack6
    side_image5.place(x=620, y=460)

    # forget Password
    # Button(signupFrame, text="forget password ?", border=False, bg="#696262", fg="white").place(x=620,y=480)


def main_signup(username_value=None):
    window = setup_windowSignUp2()
    setup_background2(window)
    signupFrame = setFramSignUp(window)
    signupComponent(signupFrame, window, username_value)
    window.mainloop()


if __name__ == "__main__":
    main_signup()
