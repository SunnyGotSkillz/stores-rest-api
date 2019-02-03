# Resources: what the app or API uses.. external representation(API interacts with it)
# Models: what makes the resources works.. internal representation (Resources can use models)

from db import db

class StoreModel(db.Model):
	__tablename__ = 'stores'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))

	items = db.relationship('ItemModel', lazy='dynamic')
	
	def __init__(self, name):
		self.name = name

	def json(self):
		return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

	@classmethod
	def find_by_name(cls, name):
		return cls.query.filter_by(name=name).first()	# builds a query in the database and does.. SELECT * FROM items WHERE name=name LIMIT 1

	def save_to_db(self):	# can upsert(update or insert) data to db
		db.session.add(self)
		db.session.commit()

	def delete_from_db(self):
		db.session.delete(self)
		db.session.commit()
		