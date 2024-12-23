import tkinter as tk
from tkinter import messagebox
def show_info():
    messagebox.showinfo("Information ","This is an important message.")
root=tk.Tk()
root.geometry("400x200+200+100")
bold_font=("Calibri",20,"bold")
button=tk.Button(root,text="Show Info",font=bold_font,command=show_info)
button.pack(pady=20)
root.mainloop()
    