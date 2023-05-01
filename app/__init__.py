from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/store')
def store():
	return render_template('store.html')

@app.route('/cart')
def cart():
	return render_template('cart.html')



