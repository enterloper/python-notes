import os
import json
from user import User

# USING JSON!
# from user import User
#
# user = User('Rich')
#
# user.add_movie('The Dark Knight', 'Action')
# user.add_movie('Gladiator', 'Adventure')
#
# with open('my_file.txt', 'r') as f:
# 	json_data = json.load(f)
# 	user = User.from_json(json_data)
# 	print(user.json())
# 	# with open('my_file.txt', 'w') as f:
# 	# json.dump(user.json(), f)

def menu():
	name = input('Enter your name: ')
	filename = '{}.txt'.format(name)

	if file_exists(filename):
		with open(filename, 'r') as f:
			json_data = json.load(f)
		user = User.from_json(json_data)
	else:
		user = User(name)

	user_input = input("Enter 'a' to add a movie, 's' to see a list of movies, "
		"'w' to set a movie as watched, 'd' to delete a movie, "
		"'l' to see the list of watched movies or 'q' to save and quit ")

	while user_input != 'q':
		if user_input == 'a':
			movie_title = input('Enter the movie name: ')
			movie_genre = input('Enter the movie genre: ')
			user.add_movie(movie_title, movie_genre)
		elif user_input == 's':
			for movie in user.movies:
				print('Title: {} Genre: {} Watched: {}'.format(movie.title, movie.genre, movie.watched))
		elif user_input == 'w':
			movie_title = input('Enter the movie name to set as watched: ')
			user.set_watched(movie_title)
		elif user_input == 'd':
			movie_title = input('Enter the movie name to delete: ')
			user.delete_movie(movie_title)
		elif user_input == 'l':
			for movie in user.watched_movies():
				print('Title: {}, Genre: {} Watched: {}'.format(movie.title, movie.genre, movie.watched))

		user_input = input("Enter 'a' to add a movie, 's' to see a list of movies, "
					   "'w' to set a movie as watched, 'd' to delete a movie, "
					   "'l' to see the list of watched movies or 'q' to save and quit ")

	with open(filename, 'w') as f:
		json.dump(user.json(), f)

def file_exists(filename):
	return os.path.isfile(filename)

menu()
