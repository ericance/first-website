from app import db

class Item(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(), nullable=False, unique=True)
	price = db.Column(db.Integer(), nullable=False)
	image = db.Column(db.String(), nullable=False, unique=True)
	quantity = db.Column(db.Integer(), nullable=False)
	def __repr__(self):
		return f'Item {self.name}'
	