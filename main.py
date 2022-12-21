from models import User, Password
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import random, string

user = User()
password = Password()
loggedInUser = None
global i
# user.add_user(('testing_user', 'randompassword'))
# user.add_user(('testing_user2', 'randompassword'))
# for i in password.read_user_data(user.get_user_id('testing_user2')):
#     for j in i:
#         print(j)
def Login():
    global loggedInUser
    if(user.check_user(usernameLog.get(), passwordLog.get())):
        loggedInUser = user.get_user_id(usernameLog.get())
        print(loggedInUser)
        usernameEntry.delete(0, 'end')
        passwordEntry.delete(0, 'end')
        mainFrame.pack()
        loginFrame.forget() 
        for row in mainFrame.grid_slaves():
            row.grid_forget()
        display()
    else:
        usernameEntry.delete(0, 'end')
        passwordEntry.delete(0, 'end')
        messagebox.showinfo("login", "Wrong password or username")
def GenerateInput():
    mainFrame.forget()
    GenerateFrame.pack()



def display():
    global i
    i = 1
    header_id = Label(mainFrame, text='id', bg="#192841", fg="#FFFFFF").grid(row=0, column=0)
    header_des = Label(mainFrame, text='Description',bg="#192841", fg="#FFFFFF").grid(row=0, column=1)
    header_user = Label(mainFrame, text='Username', bg="#192841", fg="#FFFFFF").grid(row=0, column=2)
    header_pass = Label(mainFrame, text='Password', bg="#192841", fg="#FFFFFF").grid(row=0, column=3)
    for data in password.read_user_data(loggedInUser):
        for j in range(len(data)-1):
            Lists = Label(mainFrame,width=20, text=data[j], relief='ridge')
            Lists.grid(row=i, column=j, padx=2, pady=5, sticky='s')
        delBtn = tk.Button(mainFrame, text='delete', command=lambda k=data[0]:del_data(k)).grid(row=i,column=5,padx=2, pady=5, sticky='s')
        upBtn = tk.Button(mainFrame, text='Update', command = lambda k=data[0]:update_data(k)).grid(row=i,column=6,padx=2, pady=5, sticky='s')
        i+=1
    generateButton = tk.Button(mainFrame, text="Generate", command=GenerateInput, bg="#1da1d1",fg="#FFFFFF")
    generateButton.grid(row=1000,column=0,pady=20, sticky='s')
    logoutButton = tk.Button(mainFrame, text="Logout", command=logout,bg="#1da1d1",fg="#FFFFFF")
    logoutButton.grid(row=1000, column=1, pady=20,sticky='s')
def update_data(id):
    global i
    info = password.get_data(id)
    str_id = StringVar()
    str_des = StringVar()
    str_user = StringVar()
    str_pass = StringVar()
    str_id.set(info[0])
    str_des.set(info[1])
    str_user.set(info[2])
    str_pass.set(info[3])

    id_entry = tk.Entry(mainFrame, textvariable=str_id, state='disabled', relief='ridge', justify='center').grid(row=i, column=0, padx=2, pady=5)
    id_entry = tk.Entry(mainFrame, textvariable=str_des, relief='ridge', justify='center').grid(row=i, column=1, padx=2, pady=5)
    id_entry = tk.Entry(mainFrame, textvariable=str_user, relief='ridge', justify='center').grid(row=i, column=2, padx=2, pady=5)
    id_entry = tk.Entry(mainFrame, textvariable=str_pass, relief='ridge', justify='center').grid(row=i, column=3, padx=2, pady=5)
    updateBtn = tk.Button(mainFrame, text='Update', command=lambda: update_confirm((str_des.get(), str_user.get(), str_pass.get(), str_id.get()))).grid(row=i, column=4, padx=2, pady=5)


def update_confirm(data):
    if((len(data[0]) > 4 and len(data[0]) <= 16) and (len(data[1]) > 4 and len(data[1]) <= 16) and (len(data[2]) > 4 and len(data[2]) <= 16)):
        password.update_data(data)
        for row in mainFrame.grid_slaves():
            row.grid_forget()
        display()
    else:
        messagebox.showinfo("not correct length", "all the input length have to be bigger than 4 or smaller than 16")
        for row in mainFrame.grid_slaves():
            row.grid_forget()
        display()


def del_data(id):

    password.delete_data(id)
    for row in mainFrame.grid_slaves():
        row.grid_forget()
    display()

def generate():
    if((len(Gename.get()) > 4 and len(Gename.get()) <= 16) and (len(Gedescription.get()) > 4 and len(Gedescription.get()) <= 16)):
        int_value = Gelength.get()
        try:
            int_value = int(int_value)
            if(int_value <= 16):
                password.add_password((Gedescription.get(), Gename.get(), password_generator(int_value), loggedInUser))
                GeneratenameEntry.delete(0, 'end')
                GeneratedescriptionEntry.delete(0, 'end')
                GeneratelengthEntry.delete(0, 'end')
                GenerateFrame.forget()
                mainFrame.pack()
                for row in mainFrame.grid_slaves():
                    row.grid_forget()
                display()
            else:
                messagebox.showinfo("Number too large", "the max length is 16, please try again")
        except ValueError:
            messagebox.showinfo("not number", "the Length input suppose to be in number, please try again")
    else:
        messagebox.showerror('not enough length', 'name and description have to be more than 4 character and max 16')

def password_generator(length):
  password = ""

  for i in range(length):
    password += random.choice(string.ascii_letters + string.digits + string.punctuation)

  return password



def register():
    registerFrame.pack()
    loginFrame.forget()

def logout():
    global loggedInUser
    loggedInUser = 0
    loginFrame.pack()
    mainFrame.forget()
    print("Logged out.")

def registerUser():
    if((not len(Reusername.get()) <=4 and not len(Reusername.get()) >16)and (not len(Repassword.get()) <= 4 and not len(Repassword.get()) > 16) and (not len(ReConpassword.get()) <=4 and not len(ReConpassword.get()) > 16)):
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
        messagebox.showinfo("not enough length", "all the input have to be more than 4 character and max 16")

root = tk.Tk()  
root.geometry('925x500')  

root.title('Password Generator')
root.configure(bg="#192841")

loginFrame = tk.Frame(root, bg="#192841")
mainFrame = tk.Frame(root, bg="#192841")
registerFrame = tk.Frame(root, bg="#192841")
GenerateFrame = tk.Frame(root, bg="#192841")
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
#generate frame
GenerateTitle = tk.Label(GenerateFrame, text="Password Generator", font='Arial 30',bg="#192841", fg="#FFFFFF")

GeneratedescriptionLabel = tk.Label(GenerateFrame, text='Description', font='Arial 20', bg="#192841", fg="#FFFFFF")
Gedescription = StringVar()
GeneratedescriptionEntry = tk.Entry(GenerateFrame, bd=3, textvariable=Gedescription)
GeneratenameLabel = tk.Label(GenerateFrame, text="Name",font='Arial 20', bg="#192841", fg="#FFFFFF")
Gename = StringVar()
GeneratenameEntry = tk.Entry(GenerateFrame, bd=3, textvariable=Gename)

GeneratelengthLabel = tk.Label(GenerateFrame, text="Length", font='Arial 20', bg="#192841", fg="#FFFFFF")
Gelength = StringVar()
GeneratelengthEntry = tk.Entry(GenerateFrame, bd=3, textvariable=Gelength)


generateSubmitButton = tk.Button(GenerateFrame, text="Generate", command=generate, bg="#1da1d1",fg="#FFFFFF", font='Arial 20')


#generate grid
GenerateTitle.grid(row=0, column=1, columnspan=4, padx=5, pady=40)

GeneratenameLabel.grid(row=2, column=1,padx=5,pady=5, sticky=E)
GeneratenameEntry.grid(row=2, column=2, padx=5,pady=5)

GeneratelengthLabel.grid(row=3, column=1, padx=5, pady=5, sticky=E)
GeneratelengthEntry.grid(row=3, column=2, padx=5, pady=5)

GeneratedescriptionLabel.grid(row=1, column=1, padx=5, pady=5, sticky=E)
GeneratedescriptionEntry.grid(row=1, column=2, padx=5, pady=5)

generateSubmitButton.grid(row=4, column=1, padx=5,pady=(20,5), columnspan=4, sticky= EW)
#main




root.mainloop()


