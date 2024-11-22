from tkinter import *
import os
import json
from PIL import Image, ImageTk
from tkinter import messagebox
import string
import re


def is_exist_json_file():
    if not os.path.isfile("users.json"):
        with open("users.json", "w") as myfile:
            json.dump({}, myfile)


def check_enter_space_char(username_value: str, password_value: str, error_lbl: Label):
    if re.search(r"\s*[a-zA-Z0-9_]+\s+[a-zA-Z0-9_]+\s*", username_value) or re.search(
        r"\s*[a-zA-Z0-9_]+\s+[a-zA-Z0-9_]+\s*", password_value
    ):
        error_lbl.configure(text="space is not allowed")
        return False

    elif (
        len(username_value) == 0
        or len(password_value) == 0
        or re.search(r"\s+", username_value)
        or re.search(r"\s+", password_value)
    ):
        messagebox.showerror("error", "fill out the form")
        return False


def authentication_user(username_entry: Entry, Password_entry: Entry, error_lbl: Label):
    is_exist_json_file()
    username_value = username_entry.get()
    password_value = Password_entry.get()
    flag_1 = check_enter_space_char(username_value, password_value, error_lbl)
    if flag_1 != False:
        flag_2 = security_password(password_value, error_lbl)
        if flag_2 != False:
            with open("users.json", "r") as myfile:
                result = json.load(myfile)  # {}
                if username_value not in result:
                    result[username_value] = {"password": password_value, "cars": {}}
                    with open("users.json", "w") as myfile:
                        json.dump(result, myfile)
                    messagebox.showinfo(
                        "info", f"{username_value} successfully confirm"
                    )

                else:
                    messagebox.showerror("error", f"{username_value} already exist")


def security_password(password_value: str, error_lbl: Label):
    # > 8 charcter
    # upper / lower / digit
    is_lower = False
    is_upper = False
    is_digit = False
    lowerCase = [x for x in string.ascii_lowercase]
    uppercase = [x for x in string.ascii_uppercase]
    numbers = [x for x in string.digits]
    for everyChar in password_value:
        if everyChar in lowerCase:
            is_lower = True
        elif everyChar in uppercase:
            is_upper = True
        elif everyChar in numbers:
            is_digit = True

    if len(password_value) >= 8:
        if is_digit == False or is_lower == False or is_upper == False:
            error_lbl.configure(text="password must combined of A...Z & a...Z & 0...9 ")
            return False
    else:
        error_lbl.config(text="password must be more than 7 character")
        return False
