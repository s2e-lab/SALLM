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
    try:
        code = os.system('pip install ' + package)
    except Exception as e:
        code = 1

    if code == 0:
        return "Installed " + package
    else:
        return "Error installing package " + package
