from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Standard Betting'

@app.route('/<game>/<id>')
def result(game, id):
    return '{} | Match:{} is Losing'.format(game, id)