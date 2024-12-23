import tkinter as tk

import random

def getAnswer(answerNum):
    if answerNum==1:
        return 'It is certain'
    elif answerNum==2:
        return 'It is decidely so'
    elif answerNum==3:
        return 'Yes'
    elif answerNum==4:
        return 'Try again'
    elif answerNum==5:
        return 'Ask again later'
    elif answerNum==6:
        return 'Concentrate and ask again'
    elif answerNum==7:
        return 'My reply is no'
    elif answerNum==8:
        return 'Outlook not so good'
    elif answerNum==9:
        return 'Very Doubtful'

r=random.randint(1,10)
fortune=getAnswer(r)
root=tk.Tk()
root.geometry('800x400+200+100')
root.title("Know Your Fortune!!!")
bold_font=("Algerian",18,"bold")
italic_font=("Aptos Display",18,"italic")
button=tk.Button(root,text="Click Me To Know your Fortune !",font=italic_font,command=lambda:fortune_label.config(text=fortune))
button.pack()
fortune_label=tk.Label(root,text="",font=bold_font)
fortune_label.pack()
root.mainloop()