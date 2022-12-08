import sqlite3


class User:
    def __init__(self):
        self.con = sqlite3.connect('user_pass.db')
        self.cur = self.con.cursor()
        self.create_table()
    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS Users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(25) UNIQUE,
            password VARCHAR(255)
        )
        """)
    def add_user(self, user):
        self.cur.execute("""INSERT OR IGNORE INTO Users (username, password) VALUES(?,?)""", user)
        self.con.commit()
    def get_user_id(self, username):
        self.cur.execute(f"SELECT id FROM Users WHERE username = '{username}'")
        rows = self.cur.fetchall()
        if(rows):
            return rows[0][0]
        else:
            return 0
    def check_user(self, username, password):
        if(self.get_user_id(username)):
            self.cur.execute(f"SELECT password FROM Users WHERE username = '{username}'")
            rows=self.cur.fetchall()
            if(rows[0][0] == password):
                return 1
            else:
                return 0




class Password:
    def __init__(self):
        self.con = sqlite3.connect('user_pass.db')
        self.cur = self.con.cursor()
        self.create_table()
    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS Passwords(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(25) UNIQUE,
            password VARCHAR(255),
            user_id INTEGER,
            FOREIGN KEY(user_id) REFERENCES Users(id)
        )
        """)
    def add_password(self, password):
        self.cur.execute("INSERT OR IGNORE INTO Passwords (name, password, user_id) VALUES (?,?,?)", password)
        self.con.commit()
    def read_user_data(self, user):
        self.cur.execute(f"SELECT * FROM Passwords WHERE user_id = (SELECT id FROM Users WHERE id = {user})")
        rows = self.cur.fetchall()
        return rows