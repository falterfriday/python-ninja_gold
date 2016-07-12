from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key='ivegotasecretforyou...boo!'
import random, datetime
@app.route('/')
def index():
	if not session.has_key('gold'):
		session['gold'] = 0	
	if not session.has_key('output'):
		session['output'] = ''	
	if not session.has_key('output'):
		session['output'] = ''
	gold = session['gold']
	output = session['output']
	return render_template('index.html', gold=gold, output=output)
@app.route('/process_money', methods=['POST'])
def money():
	if request.form.has_key('farm_gold'):
		random_num = random.randint(10,20)
		session['gold'] += random_num
		session['output'] += '<p class="green">Earned ' +str(random_num)+ ' golds from the farm! (' +str(datetime.datetime.now())+ ')</p>'
	elif request.form.has_key('cave_gold'):
		random_num = random.randint(5,10)
		session['gold'] += random_num
		session['output'] += '<p class="green">Earned ' +str(random_num)+ ' golds from the cave! (' +str(datetime.datetime.now())+ ')</p>'
	elif request.form.has_key('house_gold'):
		random_num = random.randint(2,5)
		session['gold'] += random_num
		session['output'] += '<p class="green">Earned ' +str(random_num)+ ' golds from the house! (' +str(datetime.datetime.now())+ ')</p>'
	elif request.form.has_key('casino_gold'):
		random_num = random.randint(-50,50)
		session['gold'] += random_num
		if random_num > 0:
			session['output'] += '<p class="green">Earned ' +str(random_num)+ ' golds from the casino! (' +str(datetime.datetime.now())+ ')</p>'
		elif random_num < 0:
			random_num = random_num * -1
			session['output'] += '<p class="red">Entered a casino and lost ' +str(random_num)+ ' golds... Ouch.. (' +str(datetime.datetime.now())+ ')</p>'
	return redirect('/')
@app.route('/clear')
def clear():
	session.clear()
	return redirect('/')
app.run(debug=True)