import tkinter as tk

class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("400x300")
        
        self.logo = tk.Label(self, text="Login here", font=("Helvetica", 15)) 
        self.logo.pack(padx=5)
        self.usernameLabel=tk.Label(self,text="Username")
        self.usernameLabel.pack(padx=5)
        self.usernameEntry=tk.Entry(self)
        self.usernameEntry.pack(padx=5)
        
        self.passwordLabel=tk.Label(self,text="Password")
        self.passwordLabel.pack(padx=5)
        self.passwordEntry=tk.Entry(self,show="*")
        self.passwordEntry.pack(padx=5)
        
        
        self.loginButton =tk.Button(self,text="login",command=self.login)
        self.loginButton.pack(padx=5)
        
        self.signupLabel=tk.Label(self,text="Don't have an account? SignUp here",fg="blue",cursor="hand2")
        self.signupLabel.pack(padx=5)
        self.signupLabel.bind("<Button-1>",self.signup)
        
    def login(self):
        username=self.usernameEntry.get()
        password=self.passwordEntry.get()
        print(f"Username:{username},Password:{password}")   
    def signup(self,event):
        print("Redirecting to SignUp page ")
if __name__=="__main__":
    LoginWindow=LoginWindow()
    LoginWindow.mainloop()            
            