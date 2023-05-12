import json
from app import app, db
from flask import render_template, request, Response
from app.models import Item

quantityTracker = 0
try:
	for item in Item.query.all():
		quantityTracker += item.quantity
except:
	pass

@app.route('/')
@app.get('/home')
def index() -> str:
	''' Returns the html template for the home page '''
	return render_template('index.html', quantity=("99+" if quantityTracker > 99 else quantityTracker))

@app.get('/store/')
def store() -> str:
	''' Returns the html template for the store page
	and populates template with items from SQL datbase '''
	items = Item.query.all()
	return render_template('store.html', items=items, quantity=("99+" if quantityTracker > 99 else quantityTracker))

@app.get('/cart')
def cart() -> str:
	''' Returns the html template for the cart page 
	and sets up JSON file with item id, name, price, and quantity '''
	items = Item.query.all()
	itemJSON = []
	itemSize = 0
	for item in items:
		itemJSON.append({
			"id": item.id,
			"name": item.name,
			"price": item.price,
			"quantity": item.quantity
		})
		if item.quantity > 0:
			itemSize += 1
	return render_template('cart.html', items=items, itemSize=itemSize, itemsJSON=json.dumps(itemJSON), quantity=("99+" if quantityTracker > 99 else quantityTracker))

@app.post('/api/cart')
def apiCart() -> int:
	''' Writes quantity of items to JSON files '''
	global quantityTracker
	quantityTracker += 1
	try:
		data = request.json
		item_id = int(data["id"])
		item_object = Item.query.filter_by(id=item_id).first()
		item_object.quantity += 1
		db.session.commit()
		return Response(status=204)
	except:
		return Response(status=500)

@app.post('/api/checkout')
def apiCheckout() -> int:
	''' Clears database '''
	global quantityTracker
	try:
		items = Item.query.all()
		quantityTracker = 0
		for item in items:
			item.quantity = 0
		db.session.commit()
		return Response(status=204)
	except Exception as e:
		print(e)
		return Response(status=500)
