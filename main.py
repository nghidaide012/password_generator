from models import User, Password
from tkinter import *
import tkinter as tk
from tkinter import messagebox

user = User()
password = Password()
loggedInUser = None
# user.add_user(('testing_user', 'randompassword'))
# user.add_user(('testing_user2', 'randompassword'))
# password.add_password(('testing','someusername', 'randomepassword', user.get_user_id('testing_user2')))
# for i in password.read_user_data(user.get_user_id('testing_user2')):
#     for j in i:
#         print(j)
def Login():
    if(user.check_user(usernameLog.get(), passwordLog.get())):
        loggedInUser = user.get_user_id(usernameLog.get())
        print(loggedInUser)
        usernameEntry.delete(0, 'end')
        passwordEntry.delete(0, 'end')
        mainFrame.pack()
        loginFrame.forget() 
    else:
        usernameEntry.delete(0, 'end')
        passwordEntry.delete(0, 'end')
        messagebox.showinfo("login", "Wrong password or username")


def generate():
    print("Your password has been generated.")

def register():
    registerFrame.pack()
    loginFrame.forget()

def logout():
    loggedInUser = None
    loginFrame.pack()
    mainFrame.forget()
    print("Logged out.")

def registerUser():
    if(not len(Reusername.get()) <=4 and not len(Repassword.get()) <= 4 and not len(ReConpassword.get()) <=4):
        if(user.get_user_id(Reusername.get()) != 0):
            messagebox.showinfo("existed user", "This user name already exists, please choose another username.")
        else:
            if(Repassword.get() != ReConpassword.get()):
                messagebox.showinfo("password", "the password and confirm password are not the same, please check again")
            else:
                user.add_user((Reusername.get(), Repassword.get()))
                ReusernameEntry.delete(0, 'end')
                RepasswordEntry.delete(0, 'end')
                RepasswordConEntry.delete(0, 'end')
                loginFrame.pack()
                registerFrame.forget()
    else:
        messagebox.showinfo("not enough length", "all the input have to be more than 4 character")

root = tk.Tk()  
root.geometry('925x500')  

root.title('Password Generator')
root.configure(bg="#192841")

loginFrame = tk.Frame(root, bg="#192841")
mainFrame = tk.Frame(root, bg="#192841")
registerFrame = tk.Frame(root, bg="#192841")

#Login
titleLabel = tk.Label(loginFrame, text="Login", font='Arial 30',bg="#192841", fg="#FFFFFF")
usernameLabel = tk.Label(loginFrame, text="Username", font='Arial 20', bg="#192841", fg="#FFFFFF")
usernameLog = StringVar()
usernameEntry = tk.Entry(loginFrame, textvariable=usernameLog, bd=3)
passwordLabel = tk.Label(loginFrame, text="Password", font='Arial 20', bg="#192841", fg="#FFFFFF")
passwordLog = StringVar()
passwordEntry = tk.Entry(loginFrame, textvariable=passwordLog, show="*",bd=3)
submitButton = tk.Button(loginFrame, text="Login", command=Login, bg="#1da1d1",fg="#FFFFFF", font='Arial 20')  
registerButton = tk.Button(loginFrame, text="Register", command=register, bg="#1da1d1",fg="#FFFFFF", font='Arial 20')

#LoginGrid
titleLabel.grid(row=0, column=0, columnspan=4, padx=5, pady=40)
usernameLabel.grid(row=1, column=0, pady=10)
usernameEntry.grid(row=1, column=1)
passwordLabel.grid(row=2, column=0, pady=10)

passwordEntry.grid(row=2, column=1)
submitButton.grid(row=3, column=0, padx=5,pady=40,sticky="ew")
registerButton.grid(row=3, column=1,padx=5,pady=40)

loginFrame.pack()

#Register
registerTitle = tk.Label(registerFrame, text="Register", font='Arial 30', bg="#192841", fg="#FFFFFF")

userLabel = tk.Label(registerFrame, text="Username", font='Arial 20', bg="#192841", fg="#FFFFFF")
Reusername = StringVar()
ReusernameEntry = tk.Entry(registerFrame, bd=3, textvariable=Reusername)

passLabel = tk.Label(registerFrame, text="Password", font='Arial 20', bg="#192841", fg="#FFFFFF")
Repassword = StringVar()
RepasswordEntry = tk.Entry(registerFrame, bd=3,show="*", textvariable=Repassword)

passConLabel = tk.Label(registerFrame, text="Confirm Password", font='Arial 20', bg="#192841", fg="#FFFFFF")
ReConpassword = StringVar()
RepasswordConEntry = tk.Entry(registerFrame, bd=3, show="*", textvariable=ReConpassword)

buttonLabel = tk.Button(registerFrame, text="Register", command=registerUser, bg="#1da1d1",fg="#FFFFFF", font='Arial 20')

#RegisterGrid
registerTitle.grid(row=0, column=1, columnspan=4, padx=5, pady=40)

ReusernameEntry.grid(row=1, column=2, padx=5, pady=5)
userLabel.grid(row=1, column=1, padx=5, pady=5, sticky=E)

RepasswordEntry.grid(row=2, column=2, padx=5, pady=5)
passLabel.grid(row=2, column=1, padx=5, pady=5, sticky=E)

RepasswordConEntry.grid(row=3, column=2, padx=5, pady=5)
passConLabel.grid(row=3, column=1, padx=5, pady=5, sticky=E)

buttonLabel.grid(row=4, column=1, padx=5, pady=5, columnspan=2, sticky='news')

#Main
mainTitle = tk.Label(mainFrame, text="Password Generator", font='Arial 30',bg="#192841", fg="#FFFFFF")
nameLabel = tk.Label(mainFrame, text="Name",font='Arial 20', bg="#192841", fg="#FFFFFF")
nameEntry = tk.Entry(mainFrame, bd=3)

lengthLabel = tk.Label(mainFrame, text="Length", font='Arial 20', bg="#192841", fg="#FFFFFF")
lengthEntry = tk.Entry(mainFrame, bd=3)

descriptionLabel = tk.Label(mainFrame, text='Description', font='Arial 20', bg="#192841", fg="#FFFFFF")
descriptionEntry = tk.Entry(mainFrame, bd=3)

generateButton = tk.Button(mainFrame, text="Generate", command=generate, bg="#1da1d1",fg="#FFFFFF", font='Arial 20')
logoutButton = tk.Button(mainFrame, text="Logout", command=logout,bg="#1da1d1",fg="#FFFFFF", font='Arial 20')

#MainGrid
mainTitle.grid(row=0, column=1, columnspan=4, padx=5, pady=40)

nameLabel.grid(row=1, column=1,padx=5,pady=5, sticky=E)
nameEntry.grid(row=1, column=2, padx=5,pady=5)

lengthLabel.grid(row=2, column=1, padx=5, pady=5, sticky=E)
lengthEntry.grid(row=2, column=2, padx=5, pady=5)

descriptionLabel.grid(row=3, column=1, padx=5, pady=5, sticky=E)
descriptionEntry.grid(row=3, column=2, padx=5, pady=5)

generateButton.grid(row=4, column=1, padx=5,pady=(20,5), columnspan=4, sticky= EW)
logoutButton.grid(row=5, column=1,padx=5, columnspan=4, sticky=EW)





root.mainloop()


