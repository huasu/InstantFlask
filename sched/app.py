from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world!'

@app.route('/appointments/')
def appointment_list():
    return 'Listing of all appointments we have.'

@app.route('/appointments/<int:appointment_id>/')
def appointment_detail(appointment_id):
    edit_url = url_for('appointment_edit',
        appointment_id = appointment_id)
    # Return the URL string just for demonstration
    return edit_url

@app.route(
    '/appointments/<int:appointment_id>/edit/',
    methods=['GET', 'POST'])

# @app.route(...) and def appointment_edit(...).

def appointment_edit(appointment_id):
    return 'Form to edit appointment #.'.format(appointment_id)

@app.route(
    '/appointments/create',
    methods=['GET', 'POST'])
def appointment_create():
    return 'Form to create a new appointment.'

@app.route(
    '/appointments/<int:appointment_id>/delete',
    methods=['DELETE'])
def appointment_delete(appointment_id):
    raise NotImplememntedError('DELETE')





if __name__ == '__main__':
    app.run('0.0.0.0', 8080)  # to access from another machine


