from app import db

class Item(db.Model):
	''' Sets up database model to define item id, name, price, image, and quantity '''
	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(), nullable=False, unique=True)
	price = db.Column(db.Integer(), nullable=False)
	image = db.Column(db.String(), nullable=False, unique=True)
	quantity = db.Column(db.Integer(), nullable=False, default=0)
	def __repr__(self) -> str:
		''' Overrides default str for printing item from <Item> <id> to <Item> <name> '''
		return f'Item {self.name}'
	