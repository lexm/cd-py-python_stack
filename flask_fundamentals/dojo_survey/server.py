from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = "bananawhatever"
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/results', methods=['POST'])
def results():
    if len(request.form['name']) < 1:
        flash("Name cannot be blank")
        return redirect('/')
    elif len(request.form['comments']) < 1:
        flash("Comments cannot be blank")
        return redirect('/')
    elif len(request.form['comments']) > 120:
        flash("Comments cannot exceed 120 characters")
        return redirect('/')
    else:
        name = request.form['name']
        location = request.form['location']
        lang = request.form['lang']
        comments = request.form['comments']
        return render_template('results.html', name=name, location=location, lang=lang, comments=comments)
app.run(debug=True)
