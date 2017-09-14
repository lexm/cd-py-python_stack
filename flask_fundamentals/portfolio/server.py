from flask import Flask
from flask import render_template

app= Flask(__name__)

@app.route('/')
def main_route():
    return render_template('index.html')

@app.route('/projects')
def project_route():
    return render_template('projects.html')

@app.route('/about')
def about_route():
    return render_template('about.html')

app.run(debug=True)

