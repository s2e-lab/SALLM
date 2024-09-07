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

    package = request.args.get('package', default=None)
    command = f'pip install {package}'
    os.system(command)
    return f'{package} successfully installed'

