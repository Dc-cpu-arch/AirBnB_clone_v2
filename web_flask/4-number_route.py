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
    ''' /c/<txt> route return -> C + <txt> '''
    return 'C {}'.format(txt.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<txt>', strict_slashes=False)
def python_route(txt='is cool'):
    ''' python/(<txt>) route return '''
    return 'Python {}'.format(txt.replace('_', ' '))


@app.route('/number/<int:num>', strict_slashes=False)
def is_num(num):
    ''' /number/<n> route return -> only if n is int '''
    return '{:d} is a number'.format(num)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
