import tkinter as tk
root=tk.Tk()
canvas=tk.Canvas(root,width=400,height=300,bg="white")
canvas.pack()

canvas.create_rectangle(50,50,150,150,fill="blue")

canvas.create_oval(200,50,300,150,fill="red")

canvas.create_line(0,0,400,300,fill="green")
root.mainloop()