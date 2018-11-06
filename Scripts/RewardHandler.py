import tkinter as tk
from PIL import ImageTk, Image


def check_if_reward_is_deserved(checkbutton_list, root):
    bool_table = []
    for item in checkbutton_list:
        bool_table.append(item.get())
    if all(bool_table):
        get_reward()
    else:
        pass


def get_reward():
    new_window = tk.Toplevel()
    new_window.title("Brawo, demonie produktywności!")

    img = (Image.open("TextFiles/reward.jpg"))
    img = img.resize((312, 416), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    label = tk.Label(new_window, image=img)
    label.pack()
    label.image = img
    message_string = "Tak trzymaj!"
    tk.Label(new_window, text=message_string).pack()
