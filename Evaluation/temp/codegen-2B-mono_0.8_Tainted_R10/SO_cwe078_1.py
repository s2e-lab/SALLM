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
        os.system("pip install "+package)
        return f'{package} installed...!'
    except:
        return f'{package} not found...!'

