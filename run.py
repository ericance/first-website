from app import app

from app import db
from app.models import Item

try:
	Item.query.all()
except:
	# add more items by using the convention Item(name, price, image)
	db.create_all()

	cookie = Item(name="Cookie", price=1.50, image="https://openclipart.org/image/800px/249534")
	donut = Item(name="Donut", price=1.00, image="https://images.vexels.com/media/users/3/291448/isolated/lists/b9e74f93541a1e41d70b16548265748d-blue-glazed-donut-color-stroke.png")
	sandwich = Item(name="Sandwich", price=4.00, image="https://www.svgrepo.com/show/356613/sandwich-03.svg")
	soda = Item(name="Soda", price=2.00, image="https://cdn-icons-png.flaticon.com/256/7511/7511411.png")
	water = Item(name="Water", price=1.00, image="https://images.vexels.com/media/users/3/259089/isolated/lists/fa80c898e7295243416b975650c23990-water-semi-flat-bottle.png")
	shirt = Item(name="Shirt", price=10.00, image="https://images.vexels.com/media/users/3/205922/isolated/lists/1036cb6305295516576e02b064b7f1b3-belgian-t-shirt-hand-drawn.png")
	pants = Item(name="Pants", price=15.00, image="https://cdn-icons-png.flaticon.com/256/2117/2117481.png")
	headphones = Item(name="Headphones", price=35.00, image="https://cdn-icons-png.flaticon.com/512/3193/3193548.png")
	computer = Item(name="Computer", price=150.00, image="https://cdn-icons-png.flaticon.com/512/3439/3439971.png")
	bongo = Item(name="Bongo", price=45, image="https://images.vexels.com/media/users/3/179131/isolated/lists/af51066440c5c0cdb5205977b59ba47d-bongo-drum-kettle-drum-flat.png")
	cat = Item(name="Cat", price=1250, image="https://i.pinimg.com/originals/82/57/4a/82574a7340693aab60228b15e34cfe13.png")
	bongoCat = Item(name="Bongo Cat", price=999.99, image="https://64.media.tumblr.com/8536b658c824f7f5ee5db70e5af1e11c/tumblr_pfa585inqo1rm7fw6o1_1280.gif")
	shiba = Item(name="Shiba", price=1500, image="https://img.rttt.net/2022/01/19/ea0030899550c.gif")
	petCrate = Item(name="Pet Crate", price=90, image="https://cdn-icons-png.flaticon.com/256/9739/9739986.png")
	petFood = Item(name="Pet Food", price=25, image="https://cdn-icons-png.flaticon.com/256/9739/9739978.png")
	succulent = Item(name="Succulent", price=15, image="https://images.vexels.com/media/users/3/181395/isolated/lists/1073b2eeae08274a9a067e88090d35b0-succulent-plant-stroke-illustration.png")
	bouqet = Item(name="Bouqet", price=5, image="https://cdn-icons-png.flaticon.com/256/7039/7039059.png")
	cactus = Item(name="Cactus", price=2.50, image="https://i.pinimg.com/originals/21/03/c7/2103c768bde91c342787fc4f78e9416b.png")

	for newItem in ['cookie', 'donut', 'sandwich', 'soda', 'water', 'shirt', 'pants', 'headphones', 'computer', 'bongo', 'cat', 'bongoCat', 'shiba', 'petCrate', 'petFood', 'succulent', 'bouqet', 'cactus']:
		db.session.add(locals()[newItem])
	db.session.commit()

if __name__ == '__main__':
	app.run(debug=True)
