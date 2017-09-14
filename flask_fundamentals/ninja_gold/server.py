from flask import Flask, render_template, session, request, redirect
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'seahawks'

@app.route('/')
def main_route():
    if not 'gold' in session:
        session['gold'] = 0
    if not 'record' in session:
        session['record'] = []
    return render_template('index.html')

@app.route('/process_money',methods=['POST'])
def money_route():
    if request.form['choice'] == 'farm':
        change = random.randint(10,20)
        session['gold'] += change
    elif request.form['choice'] == 'cave':
        change = random.randint(5,10)
        session['gold'] += change
    elif request.form['choice'] == 'house':
        change = random.randint(2,2)
        session['gold'] += change
    elif request.form['choice'] == 'casino':
        change = random.randint(-50,50)
        session['gold'] += change
    newrec = {}
    newrec['choice'] = request.form['choice']
    newrec['change'] = change
    newrec['time'] = datetime.now().strftime("%Y-%m-%d %I:%M %p")
    session['record'].append(newrec)
    return redirect('/')

app.run(debug=True)
