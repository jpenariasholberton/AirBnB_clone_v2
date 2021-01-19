#!/usr/bin/python3
""" Script that starts a Flask web application: Your web
application must be listening on 0.0.0.0, port 5000.

Routes:
    - /: display “Hello HBNB!”
    - /hbnb: display “HBNB”
    - /c/<text>: display “C ” followed by the value of the
    text variable (replace underscore _ symbols with a space )
    - You must use the option strict_slashes=False in your
    route definition"""


from flask import Flask
app = Flask(__name__)

# For all URLs
app.url_map.strict_slashes = False


# Decorator to tell Flask what URL should trigger the function.
@app.route('/')
def hello_hbnb():
    """ Output is Hello HBNB """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """ Display HBNB """
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """ Display C + text """
    strin = text.replace('_', ' ')
    return "C %s" % strin

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
