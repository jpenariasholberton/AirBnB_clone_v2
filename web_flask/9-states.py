#!/usr/bin/python3
""" """


from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_id(id=None):
    """ list the states for id """
    states = []
    list_states = storage.all(State).values()
    if id is not None:
        for state in list_states:
            if state.id == id:
                states.append(state)
    else:
        states = list_states
    return render_template('9-states.html', states=states)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ list the states """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close(self):
    """ Remove the current SQLAlchemy Session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
