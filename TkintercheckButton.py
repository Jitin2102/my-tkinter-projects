import tkinter as tk
def show_selection():
    print("Selected Option:",var1.get(),var2.get())
root=tk.Tk()
var1=tk.IntVar()
var2=tk.IntVar()
cb1=tk.Checkbutton(root,text="Option 1",variable=var1)   
cb1.pack(anchor="w")
cb2=tk.Checkbutton(root,text="Option 2",variable=var2)   
cb2.pack(anchor="w")
buttuon =tk.Button(root,text="Show Selection",command=show_selection)
buttuon.pack(pady=10)
root.mainloop()
