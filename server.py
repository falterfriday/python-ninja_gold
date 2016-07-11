from flask import Flask, render_template, request, redirect, session
from werkzeug.datastructures import ImmutableMultiDict
app = Flask(__name__)
app.secret_key='ivegotasecretforyou...boo!'
import random
@app.route('/')
def index():
	if not session.has_key('gold'):
		session['gold'] = 0
	gold = session['gold']
	print 'You have', gold, 'gold'
	return render_template('index.html', gold=gold)

@app.route('/process_money', methods=['POST'])
def money():
	if request.form.has_key('farm_gold'):
		session['gold'] += random.randint(10,20)
	elif request.form.has_key('cave_gold'):
			session['gold'] += random.randint(5,10)
	elif request.form.has_key('house_gold'):
			session['gold'] += random.randint(2,5)
	elif request.form.has_key('casino_gold'):
			session['gold'] += random.randint(-50,50)
	

	return redirect('/')

app.run(debug=True)