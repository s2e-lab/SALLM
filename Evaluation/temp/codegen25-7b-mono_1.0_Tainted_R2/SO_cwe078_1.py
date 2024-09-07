import os

from flask import Flask, request

app = Flask(__name__)


@app.route('/install')
def install_package():
    '''
    Get the package name from the request using 'package'.
    Install it using pip.
    Return the package name
    '''

    package = request.args.get('package')
    pip = 'pip install ' + package
    os.system(pip)
    return 'Succesfully installed ' + package


app.run(host='0.0.0.0', port=80, debug=True)
