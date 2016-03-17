import os
import os.path
from flask import Flask, url_for, send_from_directory, request
from flask.ext.sqlalchemy import SQLAlchemy
from sched.models import Base
from werkzeug import secure_filename

app = Flask(__name__, static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sched.db'
assets_folder = os.path.join(app.root_path, 'static')
FILE_FOLDER = assets_folder
db=SQLAlchemy(app)
db.Model = Base


@app.route('/')
def hello():
    return 'Hello, world!'


### files
@app.route('/upload/<path:filename>', methods=['GET'])
def assets(filename):
    return send_from_directory(assets_folder, filename)

@app.route('/upload/<path:filename>', methods=['POST'])
def file_attach(filename):
    filestorage = request.files['file']
    # Don't allow '..' in filename
    filename = secure_filename(filestorage.filename)
    dest = os.path.join(FILE_FOLDER, filename)
    filestorage.save(dest)
    return 'File transferred.'

###

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


