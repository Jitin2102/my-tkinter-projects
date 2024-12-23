import tkinter as tk
import random
def change_bg():
    colours=["#FF5733","#33FF57","#3357FF","#F3FF33","#FF33A6","#33FFF0","#66AD18","#AD7823","#64A325","#DBA37E","#FA590A"]
    bg_color=random.choice(colours)
    canvas.config(bg=bg_color)
    root.after(1000,change_bg)
    
root=tk.Tk()
root.title("Happy New Year 2025")
canvas=tk.Canvas(root,width=500,height=300)
canvas.pack(fill="both",expand=True)

canvas.create_text(750,400,text="Happy New Year 2025!",font=("algerian",28,"italic"),fill="black")

change_bg()

root.mainloop()