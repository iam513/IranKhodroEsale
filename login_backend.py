from tkinter import *
import json
from tkinter import messagebox
import signupPage
from PIL import Image, ImageTk
from SalePanel import *


def check_exist_user(username_entry: Entry, Password_entry: Entry, window: Tk):
    username_value = username_entry.get()
    password_value = Password_entry.get()
    with open("users.json", "r") as myfile:
        result = json.load(myfile)
        if username_value not in result:
            messagebox.showerror("error", "please check username or password")
            message = messagebox.askquestion(
                "system message", "do you want to redirect to Sign Up ?"
            )
            if message == "yes":
                window.destroy()
                signupPage.main_signup(username_value)
                
            else:
                pass
        else:
            password_db = result[username_value]['password']
            if password_db == password_value:
                window.destroy()
                main_SalePanel(username_value)
            else:
                messagebox.showerror("error", "please check username or password")
