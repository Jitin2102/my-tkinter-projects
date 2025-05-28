import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("500x400")
turn = 0
flag = 0
pressed_buttons = []  # List to keep track of pressed buttons

def change(button, index):
    global turn, flag
    pressed_buttons.append(f"Button {index + 1}")  # Track which button was pressed

    if turn == 0:
        button["text"] = "J"
        turn = 1
    else:
        button["text"] = "A"
        turn = 0
    button.config(state="disabled")
    flag += 1
    winner(index)

def winner(index):
    global flag                                                                                                                                                                                                      
    Button = (b1, b2, b3, b4, b5, b6, b7, b8, b9)     
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        
    for combo in win_combinations:
        if all(Button[i]["text"] == "J" for i in combo):
            messagebox.showinfo("Winner", f"Jitin won!\nPressed Buttons: {', '.join(pressed_buttons)}\nWinning Combination: {combo}")
            reset_game()
            return 
        if all(Button[i]["text"] == "A" for i in combo):
            messagebox.showinfo("Winner", f"Arjit won!\nPressed Buttons: {', '.join(pressed_buttons)}\nWinning Combination: {combo}")
            reset_game()
            return 
            
    if flag == 9:  # Check for tie after checking for winners
        messagebox.showinfo("Tie", f"It's a tie!\nPressed Buttons: {', '.join(pressed_buttons)}")
        reset_game()

def reset_game():
    global turn, flag, pressed_buttons
    turn = 0
    flag = 0
    pressed_buttons = []
    for button in (b1, b2, b3, b4, b5, b6, b7, b8, b9):
        button["text"] = " "
        button.config(state="active")

def exit():
    root.destroy()

b1 = tk.Button(root, text=" ", width=6, height=3, font=("arial", 18), command=lambda: change(b1, 0), bg="yellow")
b1.grid(row=2, column=4)
b2 = tk.Button(root, text=" ", width=6, height=3, font=("arial", 18), command=lambda: change(b2, 1), bg="yellow")
b2.grid(row=2, column=5)
b3 = tk.Button(root, text=" ", width=6, height=3, font=("arial", 18), command=lambda: change(b3, 2), bg="yellow")
b3.grid(row=2, column=6)
b4 = tk.Button(root, text=" ", width=6, height=3, font=("arial", 18), command=lambda: change(b4, 3), bg="yellow")
b4.grid(row=3, column=4)
b5 = tk.Button(root, text=" ", width=6, height=3, font=("arial", 18), command=lambda: change(b5, 4), bg="yellow")
b5.grid(row=3, column=5)
b6 = tk.Button(root, text=" ", width=6, height=3, font=("arial", 18), command=lambda: change(b6, 5), bg="yellow")
b6.grid(row=3, column=6)
b7 = tk.Button(root, text=" ", width=6, height=3, font=("arial", 18), command=lambda: change(b7, 6), bg="yellow")
b7.grid(row=4, column=4)
b8 = tk.Button(root, text=" ", width=6, height=3, font=("arial", 18), command=lambda: change(b8, 7), bg="yellow")
b8.grid(row=4, column=5)
b9 = tk.Button(root, text=" ", width=6, height=3, font=("arial", 18), command=lambda: change(b9, 8), bg="yellow")
b9.grid(row=4, column=6)
b10 = tk.Button(root, text="Restart", width=6, height=3, font=("arial", 16), command=reset_game, bg="light green")
b10.grid(row=3, column=1)
b11 = tk.Button(root, text="Exit", width=6, height=3, font=("arial", 16), command=exit, bg="red")
b11.grid(row=4, column=1, padx=5, pady=1)
l1 = tk.Label(root, text="First chance of Jitin:", font=("arial", 14))
l1.grid(row=1, column=1)

root.mainloop()
