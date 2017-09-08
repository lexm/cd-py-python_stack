from flask import Flask, render_template, session, request, redirect
import random
rps = ['rock','paper','scissors']

app = Flask(__name__)
app.secret_key= 'thisisnotakey'

@app.route('/')
def main_route():
    if not 'mesg' in session:
        session['wins'] = 0
        session['losses'] = 0
        session['ties'] = 0
        session['mesg'] = ''
    return render_template('index.html',wins=session['wins'],losses=session['losses'],ties=session['ties'],mesg=session['mesg'])

@app.route('/process_play',methods=['POST'])
def process():
    print "here!"
    if request.method == 'POST':
        comp_val = random.randint(0,2)
        player_val = rps.index(request.form['play'])
        if comp_val == player_val:
            session['ties'] += 1
            done = 'tie'
        elif (player_val - comp_val) % 3 == 1:
            session['wins'] += 1
            done = 'win'
        else:
            session['losses'] += 1
            done = 'LOSE'
        print "player plays:", request.form['play']
        print "comp plays:", rps[comp_val]
        mesg = 'The computer picked ' + rps[comp_val]
        mesg += ' and you picked ' + request.form['play']
        mesg += ', you ' + done + '!'
        session['mesg'] = mesg
        return redirect('/')
        
app.run(debug=True)
