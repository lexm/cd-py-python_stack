from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def main_route():
    return render_template('index.html')

@app.route('/ninja/')
def ninja_route():
    return render_template('ninja.html')

@app.route('/ninja/<color>')
def color_route(color):
    if color == 'blue':
        filename = 'img/leonardo.jpg'
    elif color == 'orange':
        filename = 'img/michelangelo.jpg'
    elif color == 'red':
        filename = 'img/raphael.jpg'
    elif color == 'purple':
        filename = 'img/donatello.jpg'
    else:
        filename = 'img/notapril.jpg'
    return render_template('color.html',filename=filename)

app.run(debug=True)
