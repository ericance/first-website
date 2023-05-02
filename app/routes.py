from app import app, db
from flask import render_template
from app.models import Item

@app.route('/')
@app.route('/home')
def index():
	return render_template('index.html')

@app.route('/store')
def store():
	items = Item.query.all()
	return render_template('store.html', items=items)

@app.route('/cart')
def cart():
	return render_template('cart.html')