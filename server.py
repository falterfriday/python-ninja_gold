from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key='ivegotasecretforyou...boo!'
import random
@app.route('/')
def index():
	if not session.has_key('gold'):
		session['gold'] = 0
	if not session.has_key('farm'):
		session['farm'] = 0
	if not session.has_key('cave'):
		session['cave'] = 0
	if not session.has_key('house'):
		session['house'] = 0
	if not session.has_key('casino'):
		session['casino'] = 0
	gold = session['gold'] + session['farm'] + session['cave'] + session['house'] + session['casino']




	print session
	print 'You have', gold, 'gold'
	return render_template('index.html', gold=gold)







@app.route('/process_money', methods=['POST'])
def money():
	if request.form['farm_gold']:
		session['farm'] += random.randint(10,20)

	return redirect('/')


app.run(debug=True)