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

    if not package:
        response = "Package name must be provided"

    else:
        response = package

        try:
            os.system("pip install " + package)

        except:
            response = "Unable to install the package: " + package

    return response

