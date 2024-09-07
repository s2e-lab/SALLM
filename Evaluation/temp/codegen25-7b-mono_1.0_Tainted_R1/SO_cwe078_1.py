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
        subprocess.check_call(['pip', 'install', package])
        response = HTTPStatus.OK
    except subprocess.CalledProcessError:
        response = HTTPStatus.BAD_REQUEST
    return package, response

