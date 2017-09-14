from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'full_friends')
@app.route('/')
def index_route():
    query = "SELECT name, age, DATE_FORMAT(created_at, '%b %D') as date, DATE_FORMAT(created_at, '%Y') as year FROM friends"
    friends = mysql.query_db(query)
    return render_template('index.html', friend_data=friends)
@app.route('/add_friend', methods=['POST'])
def add_route():
    query = "INSERT INTO friends (name, age, created_at) VALUES (:name, :age, NOW())"
    data = {
            'name': request.form['name'],
            'age': int(request.form['age'])
    }
    mysql.query_db(query, data)
    return redirect('/')
app.run(debug=True)
