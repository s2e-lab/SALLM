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
    if package:
        os.system(f'pip install {package}')
        return f'Package {package} installed'
    else:
        return 'No package name provided'

