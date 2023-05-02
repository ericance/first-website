from app import app

from app import db
from app.models import Item

try:
	Item.query.all()
except:
	# add more items by using the convention Item(name, price, image)
	db.create_all()

	cookie = Item(name='Cookie', price=1.50, image="https://i.ibb.co/ZYhNcVf/cookie.png")
	sandwich = Item(name='Sandwich', price=4.00, image="https://i.ibb.co/TM0DSrs/sandwich.png")
	water = Item(name='Water', price=1.00, image="https://i.ibb.co/Dp6zFtk/water.png")
	db.session.add(cookie)
	db.session.add(sandwich)
	db.session.add(water)
	db.session.commit()

if __name__ == '__main__':
	app.run(debug=True)
