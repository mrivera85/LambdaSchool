from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/birthday')
def birthday():
    return 'October 04 1985'

@app.route('/greeting/<name>')
def greeting(name):
    return 'Hello ' + name
