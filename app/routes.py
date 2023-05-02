from app import app, db
from flask import render_template, request
from app.models import Item


quantityTracker=0
try:
	for item in Item.query.all():
		quantityTracker += item.quantity
except:
	pass

@app.route('/')
@app.route('/home')
def index():
	return render_template('index.html', quantity=("99+" if quantityTracker > 99 else quantityTracker))

@app.route('/store/', methods=['GET', "POST"])
def store():
	items = Item.query.all()
	if request.method == 'POST':
		global quantityTracker
		quantityTracker += 1
		try:
			data = request.json
			item_id = int(data["id"])
			item_object = Item.query.filter_by(id=item_id).first()
			item_object.quantity += 1
			db.session.commit()
		except:
			pass
	return render_template('store.html', items=items, quantity=("99+" if quantityTracker > 99 else quantityTracker))

@app.route('/cart')
def cart():
	items = Item.query.all()
	return render_template('cart.html', items=items, quantity=("99+" if quantityTracker > 99 else quantityTracker))
