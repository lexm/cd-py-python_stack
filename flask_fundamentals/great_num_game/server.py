from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "asdf_qwerty"

@app.route('/')
def main_route():
    if not 'text' in session:
        session['text'] = ''
        session['style'] = ''
        session['style2'] = 'class=hidden'
    if not 'num' in session:
        session['num'] = random.randint(1,100)
    return render_template('index.html')

@app.route('/guess',methods=['POST'])
def guess_route():
    if not 'num' in session:
        return redirect('/')
    guess = int(request.form['guess'])
    if guess > session['num']:
        session['text'] = 'Too high!'
        session['style'] = 'class=red'
    elif guess < session['num']:
        session['text'] = 'Too low!'
        session['style'] = 'class=red'
    else:
        session['text'] = str(guess) + ' was the number!'
        session['style'] = 'class=green'
        session['style2'] = ''
    return redirect('/')

@app.route('/reset')
def reset_route():
    session.clear()
    return redirect('/')

app.run(debug=True)
