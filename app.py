from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="Home")

@app.route('/<game>/<id>')
def result(game, id):
    return '{} | Match:{} is Losing'.format(game, id)