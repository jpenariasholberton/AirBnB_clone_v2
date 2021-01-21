#!/usr/bin/python3
""" script that starts a Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """ states and cities """
    st = storage.all(State).values()
    am = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=st, amenities=am)


@app.teardown_appcontext
def close(self):
    """ Remove the current SQLAlchemy Session """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
