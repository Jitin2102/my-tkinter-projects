import tkinter as tk
def show_selection():
    print("Selected Option:",var.get())
root=tk.Tk()
var =tk.StringVar(value="Option 1")
rb1=tk.Radiobutton(root,text="Option 1",variable=var,value="Option 1")   
rb1.pack(anchor="w")
rb2=tk.Radiobutton(root,text="Option 2",variable=var,value="Option 2")   
rb2.pack(anchor="w")
buttuon =tk.Button(root,text="Show Selection",command=show_selection)
buttuon.pack(pady=10)
root.mainloop()
