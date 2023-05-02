from app import app, db
from flask import render_template, request
from app.models import Item

itemKey = {
	1: "Cookie",
    2: "Sandwich",
    3: "Water"
}

@app.route('/')
@app.route('/home')
def index():
	return render_template('index.html')

@app.route('/store', methods=['GET', "POST"])
def store():
	items = Item.query.all()
	if request.method == 'POST':
		try:
			data = request.json
			item_id = int(data["id"])
			item_object = Item.query.filter_by(name=itemKey[item_id]).first()
			item_object.quantity += 1
			db.session.commit()
		except:
			pass
	return render_template('store.html', items=items)

@app.route('/cart')
def cart():
	return render_template('cart.html')

