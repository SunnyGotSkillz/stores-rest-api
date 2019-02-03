# Resources: what the app or API uses.. external representation(API interacts with it)
# Models: what makes the resources works.. internal representation (Resources can use models)

import sqlite3
from db import db

class UserModel(db.Model):		# this is technically an API because the other files use this interface to communicate
	__tablename__ = 'users' 	# link db to SQL table

	id = db.Column(db.Integer, primary_key=True)  # creates a column of type integar that has values that are unique
	username = db.Column(db.String(80))
	password = db.Column(db.String(80))

	def __init__(self, username, password):
		self.username = username
		self.password = password

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()

	@classmethod
	def find_by_username(self, username):
		return self.query.filter_by(username=username).first()

	@classmethod
	def find_by_id(self, _id):
		return self.query.filter_by(id=_id).first()