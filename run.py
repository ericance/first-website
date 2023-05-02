from app import app

from app import db
from app.models import Item

try:
	Item.query.all()
except:
	# add more items by using the convention Item(name, price, image)
	db.create_all()

	cookie = Item(name='Cookie', price=1.50, image="https://openclipart.org/image/800px/249534", quantity=0)
	sandwich = Item(name='Sandwich', price=4.00, image="https://www.svgrepo.com/show/356613/sandwich-03.svg", quantity=0)
	water = Item(name='Water', price=1.00, image="https://images.vexels.com/media/users/3/259089/isolated/lists/fa80c898e7295243416b975650c23990-water-semi-flat-bottle.png", quantity=0)
	shirt = Item(name="Tee", price=10.00, image="https://images.vexels.com/media/users/3/205922/isolated/lists/1036cb6305295516576e02b064b7f1b3-belgian-t-shirt-hand-drawn.png", quantity=0)
	db.session.add(cookie)
	db.session.add(sandwich)
	db.session.add(water)
	db.session.add(shirt)
	db.session.commit()

if __name__ == '__main__':
	app.run(debug=True)
