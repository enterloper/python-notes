from database import Database
from user import User

Database.initialise(database="learning", user="rich", password="NegroniTwo!414", host='127.0.0.1')

# my_user = User.load_from_db_by_email('cleverjam@gmail.com')
my_user = User('varma.buddaharuju@infolob.com', 'Varma', 'Buddarharuju', None)

my_user.save_to_db()

user_from_db = User.load_from_db_by_email('richardjboothe@gmail.com')

print(user_from_db)
