from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re, hashlib
import logging
# logging.BasicConfig(level=logging.DEBUG, '%(asctime)s - %(messagelevel)s - %(message)s')
NAME_REGEX = re.compile(r'^[a-zA-Z]{2,}$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'truckfump'
mysql = MySQLConnector(app, 'the_wall')

@app.route('/')
def main_route():
    print session['err']
    if not 'login' in session:
        session['login'] = False
    return render_template('login.html')

@app.route('/switch', methods=['GET'])
def switch_page():
    session['login'] = not session['login']
    session['err'] = None
    return redirect('/')

@app.route('/register', methods=['POST'])
def reg_route():
    print request.form
    session['err'] = None
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    newpass = request.form['newpass']
    confirm = request.form['confirm']
    if not (NAME_REGEX.match(fname) and NAME_REGEX.match(lname)):
        session['err'] = 'name'
    elif not EMAIL_REGEX.match(email):
        session['err'] = 'email'
    elif not len(newpass) >= 8:
        session['err'] = 'pass_len'
    elif not newpass == confirm:
        session['err'] = 'pass_match'
    else:
        hash = hashlib.md5(newpass).hexdigest()
        query = 'INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:fname, :lname, :email, :hash, NOW(), NOW())'
        data = {
                'fname': fname,
                'lname': lname,
                'email': email,
                'hash': hash
        }
        mysql.query_db(query, data)
        session['err'] = None
    print session['err']
    return redirect('/')

@app.route('/login', methods=['POST'])
def login_route():
    session['err'] = None
    login = request.form['login']
    password = request.form['password']
    hash = hashlib.md5(password).hexdigest()
    query = 'SELECT * FROM users WHERE email =  :login'
    data = { 'login': login }
    resp = mysql.query_db(query, data)
    print resp[0]
    if resp[0]['password'] == hash:
        print 'Success!'
        session['user'] = resp[0]
        session['login'] = login
        return redirect('/wall')
    session['err'] = 'login'
    return redirect('/')

@app.route('/wall')
def wall_route():
    query = 'SELECT first_name, last_name, message, DATE_FORMAT(messages.created_at, "%M %D %Y") AS date FROM messages JOIN users ON users.id = messages.user_id'
    msgs = mysql.query_db(query)
    return render_template('wall.html', msgs=msgs)

@app.route('/postmsg', methods=['POST'])
def msg_route():
    newmsg = request.form['message']
    query = 'INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user, :message, NOW(), NOW())'
    data = {
            'user': session['user']['id'],
            'message': newmsg,
    }
    mysql.query_db(query, data)
    return redirect('/wall')

app.run(debug=True)
