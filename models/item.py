# Resources: what the app or API uses.. external representation(API interacts with it)
# Models: what makes the resources works.. internal representation (Resources can use models)

from db import db

class ItemModel(db.Model):
	__tablename__ = 'items'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))
	price = db.Column(db.Float(precision=2))	# float number with two decimal places

	store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
	store = db.relationship('StoreModel')
	
	def __init__(self, name, price, store_id):
		self.name = name
		self.price = price
		self.store_id = store_id

	def json(self):
		return {'name': self.name, 'price': self.price}

	@classmethod
	def find_by_name(cls, name):
		return cls.query.filter_by(name=name).first()	# builds a query in the database and does.. SELECT * FROM items WHERE name=name LIMIT 1

	def save_to_db(self):	# can upsert(update or insert) data to db
		db.session.add(self)
		db.session.commit()

	def delete_from_db(self):
		db.session.delete(self)
		db.session.commit()
		