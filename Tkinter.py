import tkinter as tk
from functools import partial
def call_result(label_result,n1,n2):
    num1=(n1.get())
    num2=(n2.get())
    result=int(num1)+int(num2)
    label_result.config(text="Result=%d" % result ) 
    return 
root =tk.Tk()
root.geometry('400x200+100+200')
root.title('Addition')
number1=tk.StringVar()
number2=tk.StringVar()
labelNum1=tk.Label(root,text="First Number").grid(row=1,column=0)
labelNum2=tk.Label(root,text="Second Number").grid(row=2,column=0)
labelResult=tk.Label(root)
labelResult.grid(row=7,column=2)
entryNum1=tk.Entry(root,textvariable=number1).grid(row=1,column=2)
entryNum2=tk.Entry(root,textvariable=number2).grid(row=2,column=2)
call_result=partial(call_result,labelResult,number1,number2)
buttonCall=tk.Button(root,text="Addition",command=call_result).grid(row=3,column=2)
root.mainloop()


