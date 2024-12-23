import tkinter as tk
root=tk.Tk()
root.title('New')
root.geometry("200x100+200+100")
var=tk.StringVar()
lbl=tk.Label(root,textvariable=var,relief='raised')
var.set("Hey! I am Chongu.")
lbl.pack()
root.mainloop()

    

