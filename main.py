from models import User, Password
from tkinter import *
import tkinter as tk

user = User()
password = Password()

user.add_user(('testing_user', 'randompassword'))
user.add_user(('testing_user2', 'randompassword'))

password.add_password(('testing', 'randomepassword', user.get_user_id('testing_user2')))

for i in password.read_user_data(user.get_user_id('testing_user2')):
    print(i)

def submit():
    print("Username entered :", username.get())
    print("Password entered :", password.get())
    if(user.check_user(username.get(), password.get())):
        print('Logged in.')
        usernameEntry.delete(0, 'end')
        passwordEntry.delete(0, 'end')
        mainFrame.pack()
        loginFrame.forget()
    
      
    else:
        print("Try Again.")


def generate():
    print("Your password has been generated.")

def register():
    print("Registered.")

def logout():
    loginFrame.pack()
    mainFrame.forget()
    print("Logged out.")


root = tk.Tk()  
root.geometry('440x540')  
root.title('Password Generator')
root.configure(bg="#192841")

loginFrame = tk.Frame(root, bg="#192841")
mainFrame = tk.Frame(root, bg="#192841")

#Login
titleLabel = tk.Label(loginFrame, text="Login", font='Arial 30',bg="#192841", fg="#FFFFFF")
usernameLabel = tk.Label(loginFrame, text="Username", font='Arial 20', bg="#192841", fg="#FFFFFF")
username = StringVar()
usernameEntry = tk.Entry(loginFrame, textvariable=username, font='Arial 15')
passwordLabel = tk.Label(loginFrame, text="Password", font='Arial 20', bg="#192841", fg="#FFFFFF")
password = StringVar()
passwordEntry = tk.Entry(loginFrame, textvariable=password, show="*", font='Arial 15')
submitButton = tk.Button(loginFrame, text="Login", command=submit, bg="#1da1d1",fg="#FFFFFF", font='Arial 20')  
registerButton = tk.Button(loginFrame, text="Register", command=register, bg="#1da1d1",fg="#FFFFFF", font='Arial 20')


titleLabel.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
usernameLabel.grid(row=1, column=0, pady=10)
usernameEntry.grid(row=1, column=1)
passwordLabel.grid(row=2, column=0, pady=10)
passwordEntry.grid(row=2, column=1)
submitButton.grid(row=3, column=0, pady=40)
registerButton.grid(row=3, column=1)

loginFrame.pack()

#Main
titleLabel = tk.Label(mainFrame, text="Password Generator", font='Arial 30',bg="#192841", fg="#FFFFFF")
titleLabel.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)

generateButton = tk.Button(mainFrame, text="Generate", command=generate, bg="#1da1d1",fg="#FFFFFF", font='Arial 20')
logoutButton = tk.Button(mainFrame, text="Logout", command=logout,bg="#1da1d1",fg="#FFFFFF", font='Arial 20')

generateButton.grid(row=3, column=0, pady=20)
logoutButton.grid(row=3, column=1)


root.mainloop()


