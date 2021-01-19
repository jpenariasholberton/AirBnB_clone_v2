#!/usr/bin/python3
""" Script that starts a Flask web application: Your web
application must be listening on 0.0.0.0, port 5000.

Routes:
    /: display “Hello HBNB!”
    You must use the option strict_slashes=False in your
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
