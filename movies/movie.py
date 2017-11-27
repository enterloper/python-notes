class Movie:
	def __init__(self, title, genre, watched):
		self.title = title
		self.genre = genre
		self.watched = watched

	def __repr__(self):
		return '<Movie {}>'.format(self.title)

	def json(self):
		return {
			'title': self.title,
			'genre': self.genre,
			'watched': self.watched
		}

	@classmethod
	def from_json(cls, json_data):  # {'title': '...', 'genre': '...', 'watched': True}
		return Movie(title=json_data['title'], genre=json_data['genre'], watched=json_data['watched'])