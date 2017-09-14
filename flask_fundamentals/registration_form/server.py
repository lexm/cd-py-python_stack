from flask import Flask, render_template, redirect, request, session, flash
import re

app = Flask(__name__)
app.secret_key = "hereitsiwhatisit"
BAD_NAME_REGEX = re.compile(r'[0-9]')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def main_route():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    print request.form
    for field in request.form:
        if len(request.form[field]) < 1:
            flash('Field ' + field + ' cannot be blank')
            return redirect('/')
    for name_field in ['first_name', 'last_name']:
        print name_field, request.form[name_field]
        print BAD_NAME_REGEX.search(request.form[name_field])
        if BAD_NAME_REGEX.search(request.form[name_field]):
            flash('Names cannot contain numbers')
            return redirect('/')
    if len(request.form['password_1']) > 8:
        flash('Passwords cannot have more than 8 characters')
        return redirect('/')
    if not EMAIL_REGEX.match(request.form['email']):
        flash('Email address is invalid')
        return redirect('/')
    if request.form['password_1'] != request.form['password_2']:
        flash('Passwords do not match')
        return redirect('/')
    return render_template('thankyou.html')

app.run(debug=True)
