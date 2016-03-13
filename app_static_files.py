import os.path
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder=None) # disables built in static handler.
assets_folder = os.path.join(app.root_path, 'assets')

@app.route('/assets/<path:filename>')
def assets(filename):
    return send_from_directory(assets_folder, filename)



if __name__ == '__main__':
    app.run('0.0.0.0', 8080)  # to access from another machine
