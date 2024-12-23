import tkinter as tk
def show_value(val):
    print("Selected Value:",val)
root=tk.Tk() 
scale=tk.Scale(root,from_=0 ,to=100,orient="horizontal",command=show_value) 
scale.pack(pady=20)
root.mainloop()
  