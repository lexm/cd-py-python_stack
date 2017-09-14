from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "nevermind"

@app.route('/')
def main_route():
    if not 'num' in session:
        session['num'] = 0
    else:
        session['num'] += 1
    return render_template('index.html')

@app.route('/more',methods=['POST'])
def more():
    if request.form['more'] == '+2':
        session['num'] += 1
    elif request.form['more'] =="Reset":
        del session['num']
    return redirect('/')

app.run(debug=True)
