import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.title("Button Widget")
#root.geometry("1000x500+200+100")


italic_font=("Times New Roman",20,"italic")
def text():
    messagebox.showinfo("Info","I hope .You have become happy after pressing this heavenly button made by me.\n\nThanks for choosing it.\n\nAnyway you have no options to choose different button.")
    
my_button=tk.Button(root,text="Click here",font=("Calibri",10,"italic"),width=8,height=2,command=text)
#my_button=tk.Button(root,text="Click here",font=("Calibri",10,"italic"),width=8,height=2,command =lambda:label.Config(text="I hope .You have become happy after pressing this heavenly button made by me.\n\nThanks for choosing it.\n\nAnyway you have no options to choose different button."))

my_button.pack(pady=10) 
#label=tk.Label(root,text="",font=italic_font)
#label.pack()
root.mainloop()           
