import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):

	parser = reqparse.RequestParser()
	parser.add_argument(
		'username',
		type=str,
		required=True,
		help="Username needed to complete request!"
	)
	parser.add_argument(
		'password',
		type=str,
		required=True,
		help="Password needed to complete request!"
	)

	def post(self):
		data = UserRegister.parser.parse_args()

		if UserModel.find_by_username(data['username']):
			return {"message": "That username already exists"}, 400

		user = UserModel(**data)
		user.save_to_db()

		return {"message": "User created successfully."}, 201
