from flask import Flask, request, redirect, render_template, session
from mysqlconnection import MySQLConnector
import re, hashlib
NAME_REGEX = re.compile(r'^[a-zA-Z]{2,}$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'truckfump'
mysql = MySQLConnector(app, 'login_registration')
@app.route('/')
def main_route():
    print session
    return render_template('index.html')
@app.route('/register', methods=['POST'])
def reg_route():
    session['err'] = None
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['login']
    password = request.form['password']
    confirm = request.form['confirm']
    print fname, lname, email, password, confirm
    print NAME_REGEX.match(fname), NAME_REGEX.match(lname), EMAIL_REGEX.match(email)
    if not (NAME_REGEX.match(fname) and NAME_REGEX.match(lname)):
        session['err'] = 'name'
    elif not EMAIL_REGEX.match(email):
        session['err'] = 'email'
    elif not len(password) >= 8:
        session['err'] = 'pass_len'
    elif not password == confirm:
        session['err'] = 'pass_match'
    else:
        hash = hashlib.md5(password).hexdigest()
        query = 'INSERT INTO users (first_name, last_name, email, hash, created_at, updated_at) VALUES (:fname, :lname, :email, :hash, NOW(), NOW())'
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
app.run(debug=True)
