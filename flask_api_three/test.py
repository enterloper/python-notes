import sqlite3

connection = sqlite3.connect('database.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, 'Jenny', 'asdf')

insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

users = [
	(1, 'Bob', 'hjkl'),
	(1, 'Rich', 'zxy')
]

cursor.executemany(insert_query, users)

select_query = "SELECT * from users"

for row in cursor.execute(select_query):
	print(row)

connection.commit()

connection.close()
