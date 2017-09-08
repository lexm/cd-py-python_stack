from flask import Flask, render_template, session, request, redirect
import random
rps = ['rock','paper','scissors']

app = Flask(__name__)
app.secret_key= 'thisisnotakey'

@app.route('/')
def main_route():
    if not 'wins' in session:
        session['wins'] = 0
        session['losses'] = 0
        session['ties'] = 0
    return render_template('index.html',wins=session['wins'],losses=session['losses'],ties=session['ties'])

@app.route('/process_play',methods=['POST'])
def process():
    if request.method == 'POST':
        comp_val = random.randint(0,2)
        player_val = rps.index(request.form['play'])
        if comp_val == player_val:
            session['ties'] += 1
        elif (player_val - comp_val) % 3 == 1:
            session['wins'] += 1
        else:
            session['losses'] += 1
        print "player plays:", request.form['play']
        print "comp plays:", rps[comp_val]
        redirect('/')
        
app.run(debug=True)
