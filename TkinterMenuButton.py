import tkinter as tk

root=tk.Tk()
root.geometry("400x200+200+100")

mb=tk.Menubutton(root,text="Options",relief="raised")
mb.grid(row=200,column=100)
mb.menu=tk.Menu(mb,tearoff=0)
mb["menu"]=mb.menu
momoVar=tk.IntVar()
ketchVar=tk.IntVar()
mb.menu.add_checkbutton (label="momos",variable=momoVar)
mb.menu.add_checkbutton (label="ketchup",variable=ketchVar)

mb.pack()
root.mainloop()
