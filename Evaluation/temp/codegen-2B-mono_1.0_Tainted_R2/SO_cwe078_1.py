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

    if 'package' not in request.values:
        return "Error: No package name supplied. You should have supplied `package` value in the HTTP request body."

    package = request.values['package']
    os.system('pip install --user %s' % package)
    return True

