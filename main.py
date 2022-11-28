from models import User, Password

user = User()
password = Password()

user.add_user(('testing_user', 'randompassword'))
user.add_user(('testing_user2', 'randompassword'))

password.add_password(('testing', 'randomepassword', user.get_user_id('testing_user2')))

for i in password.read_user_data(user.get_user_id('testing_user2')):
    print(i)