#!/usr/bin/python3
''' script that starts a Flask web application '''
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    ''' root route return '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    ''' /hbnb route return '''
    return 'HBNB'


@app.route('/c/<txt>', strict_slashes=False)
def c_route(txt):
    ''' /c/<text> route return -> C + <txt>'''
    return 'C {}'.format(txt.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
