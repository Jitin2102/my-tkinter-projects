import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
import csv

def load_csv_data():
    with open('new.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            tree.insert("", tk.END, values=row)

def show_treeview():
    password = simpledialog.askstring("Password", "Enter developer password:", show='*')
    if password == "jitin@123":  # Change this to your developer password
        tree.grid()
        toggle_button.config(state=tk.DISABLED)
    else:
        messagebox.showerror("Error", "Invalid Password")

def Login():
    name = entry1.get()
    username = entry6.get()
    email = entry3.get()
    contact = entry4.get()
    password = entry2.get()
    reEnterpassword = entry7.get()
    
    if password != reEnterpassword:
        messagebox.showerror("Invalid Error", "Password not matched")
        entry2.delete(0,tk.END)
        entry7.delete(0,tk.END)
    elif not name or not username or not password or not email or not contact:
        messagebox.showerror("Error", "Enter all asked details")
    else:
        # Print to terminal for debugging
        print(f"Name: {name}\nEmail:{email}\nContact Number:{contact}\nUsername: {username}\nPassword: {password}")
        
        # Save the information to the CSV file
        with open('new.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([name, username, password, contact, email])
        
        # Clear the entry fields after saving
        entry1.delete(0, tk.END)
        entry6.delete(0, tk.END)
        entry3.delete(0, tk.END)
        entry4.delete(0, tk.END)
        entry2.delete(0, tk.END)
        entry7.delete(0, tk.END)
        
        # Reload the data into the Treeview
        for row in tree.get_children():
            tree.delete(row)
        load_csv_data()
    
root = tk.Tk()
root.title("instaBlame")
root.geometry("500x600+200+100")  # Adjusted for 15.6-inch laptop display
fonts = ("Times New Roman", 15, "bold")

label0 = tk.Label(root, text="Welcome to InstaBlame", font=fonts, fg="red")
label0.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

label1 = tk.Label(root, text="Name:", font=fonts)
label1.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
entry1 = tk.Entry(root, bd=2)
entry1.grid(row=1, column=1, padx=5, pady=5)

label3 = tk.Label(root, text="Enter Email:", font=fonts)
label3.grid(row=2, column=0, sticky=tk.E, padx=5, pady=5)
entry3 = tk.Entry(root, bd=2)
entry3.grid(row=2, column=1, padx=5, pady=5)

label4 = tk.Label(root, text="Contact Number:", font=fonts)
label4.grid(row=3, column=0, sticky=tk.E, padx=5, pady=5)
entry4 = tk.Entry(root, bd=2)
entry4.grid(row=3, column=1, padx=5, pady=5)

gender_var = tk.StringVar(root)
label5 = tk.Label(root, text="Gender:", font=fonts)
label5.grid(row=4, column=0, sticky=tk.E, padx=5, pady=5)
gender_var.set("Select Gender")
gender_options = ['Male', 'Female', 'Other']
gender_menu = tk.OptionMenu(root, gender_var, *gender_options)
gender_menu.grid(row=4, column=1, padx=5, pady=5)

label6 = tk.Label(root, text="Username:", font=fonts)
label6.grid(row=5, column=0, sticky=tk.E, padx=5, pady=5)
entry6 = tk.Entry(root, bd=2)
entry6.grid(row=5, column=1, padx=5, pady=5)

label2 = tk.Label(root, text="Password:", font=fonts)
label2.grid(row=6, column=0, sticky=tk.E, padx=5, pady=5)
entry2 = tk.Entry(root, bd=2, show="*")
entry2.grid(row=6, column=1, padx=5, pady=5)

label7 = tk.Label(root, text="Re-enter Password:", font=fonts)
label7.grid(row=7, column=0, sticky=tk.E, padx=5, pady=5)
entry7 = tk.Entry(root, bd=2, show="*")
entry7.grid(row=7, column=1, padx=5, pady=5)

button = tk.Button(root, text="Login",font=fonts,fg="green",command=Login)
button.grid(row=8, column=1, columnspan=2, pady=5)

button =tk.Button(root,text="SignUp",fg="red",font=fonts,command=lambda :label.config(text="Redirecting to SignUp Page"))
button.grid(row=9,column=2,padx=5,pady=5)
label=tk.Label(root,text="Don't have an account?",fg="blue",font=fonts)
label.grid(row=9,column=0,columnspan=2,pady=5)
label=tk.Label(root,text="",font=fonts)
label.grid(row=10,column=1,columnspan=2,pady=5)

# Button to show Treeview
toggle_button = tk.Button(root, text="Show CSV Data", command=show_treeview)
toggle_button.grid(row=11, column=0)

# Create a Treeview widget to display the data
tree = ttk.Treeview(root, columns=("Name", "Username", "Password", "Contact", "Email"), show='headings')
tree.heading("Name", text="Name")
tree.heading("Username", text="Username")
tree.heading("Password", text="Password")
tree.heading("Contact", text="Contact")
tree.heading("Email", text="Email")

# Initially hide the Treeview widget
tree.grid(row=12, column=0, columnspan=2, sticky="nsew")
tree.grid_remove()

# Configure grid row and column weights for the Treeview
root.rowconfigure(10, weight=1)

# Load the CSV data into the Treeview
load_csv_data()

root.mainloop()