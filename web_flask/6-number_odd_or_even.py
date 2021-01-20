#!/usr/bin/python3
""" Script that starts a Flask web application: Your web
application must be listening on 0.0.0.0, port 5000.

Routes:
    - /: display “Hello HBNB!”
    - /hbnb: display “HBNB”
    - /c/<text>: display “C ” followed by the value of the
    text variable (replace underscore _ symbols with a space )
    - /python/(<text>): display “Python ”, followed by the
    value of the text variable (replace underscore _ symbols with a space )
        The default value of text is “is cool”
    - /number/<n>: display “n is a number” only if n is an integer
    - /number_template/<n>: display a HTML page only if n is an integer:
        H1 tag: “Number: n” inside the tag BODY
    - /number_odd_or_even/<n>: display a HTML page only if n is an integer:
        H1 tag: “Number: n is even|odd” inside the tag BODY
    - You must use the option strict_slashes=False in your
    route definition"""


from flask import Flask, render_template
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
    txt = text.replace('_', ' ')
    return "C %s" % txt


@app.route('/python')
@app.route('/python/<text>')
def python_text(text="is cool"):
    """ Display default python + text """
    txt = text.replace('_', ' ')
    return "Python %s" % txt


@app.route('/number/<int:n>')
def number_n(n):
    """ Display “n is a number” """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def num_template(n):
    """ Dispays a number template """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def num_odd_or_even(n):
    """ Display a HTML numer odd or even """
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
