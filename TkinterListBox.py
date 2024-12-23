import tkinter as tk

root=tk.Tk()
root.title('ListBox')
root.geometry("300x200")
lb1=tk.Listbox(root)
lb1.insert(1,"Python")
lb1.insert(2,"Java")
lb1.insert(3,"C")         #  NOT WORKING WHY ?
lb1.insert(4,"C++")
lb1.insert(5,"HTML")
lb1.insert(6,"CSS")
lb1.insert(7,"Javascript")
lb1.pack()
root.mainloop()