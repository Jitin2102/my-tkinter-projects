import tkinter as tk

root=tk.Tk()
root.title('Entry Widget')
root.geometry("400x300+200+100")
font=("Times New Roman",10) 
l1=tk.Label(root,text="User Id",font=font)
l2=tk.Label(root,text="Password",font=font)

l1.grid(row=50,column=40)
l2.grid(row=60,column=40)

E1=tk.Entry(root,bd=5)
E2=tk.Entry(root,bd=5)

E1.grid(row=50,column=50)
E2.grid(row=60,column=50)
root.mainloop()


