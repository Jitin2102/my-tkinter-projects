import tkinter as tk
root=tk.Tk()
root.title("Buttons")
root.geometry("400x300+200+100")
frame=tk.Frame(root)
frame.pack()
bottomframe=tk.Frame(root)
bottomframe.pack(side='bottom')

redbutton=tk.Button(frame,text="Red",fg="red")
redbutton.pack(side="left")

greenbutton=tk.Button(frame,text="Green",fg="green")
greenbutton.pack(side="right")

yellowbutton=tk.Button(frame,text="Blue",fg="blue")
yellowbutton.pack(side="left")

root.mainloop()