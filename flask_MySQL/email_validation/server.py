from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'Not a secret!'
mysql = MySQLConnector(app, 'email_valid')
@app.route('/')
def index_route():
    query = "SELECT *, DATE_FORMAT(created_at, '%m/%d/%y %h:%i%p') as date FROM email"
    addresses = mysql.query_db(query)
    print session
    return render_template('index.html', addys=addresses)
@app.route('/email', methods=['POST'])
def email_route():
    entry = request.form['email']
    if len(entry) < 1:
        session['notblank'] = False
    elif not EMAIL_REGEX.match(entry):
        session['valid'] = False
        session['notblank'] = True
    else:
        query = "INSERT INTO email (email, created_at, updated_at) VALUES (:entry, NOW(), NOW());"
        data = { 'entry': entry }
        mysql.query_db(query, data)
        session['valid'] = True
        session['notblank'] = True
        session['last'] = entry
    return redirect('/')
app.run(debug=True)
