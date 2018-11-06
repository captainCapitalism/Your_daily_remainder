import tkinter as tk


def setup_root():
    root = tk.Tk()
    root.title("Jazda do roboty, chamy!")
    root.resizable(width=False,
                   height=True)

    return root


def setup_frame(master):
    frame = tk.Frame(master)
    frame.grid(row=0, column=0,
               sticky="news", padx=50)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_columnconfigure(2, weight=1)

    return frame
