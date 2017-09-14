from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def main_route():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_route():
    name = request.form['name']
    print 'Name is:', name
    return redirect('/')

app.run(debug=True)
