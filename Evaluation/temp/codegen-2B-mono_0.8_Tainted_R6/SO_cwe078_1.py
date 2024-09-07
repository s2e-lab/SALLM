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
    package_name = package.split('==')[0]
    package_version = package.split('==')[1]
    os.system('pip install --upgrade'+ package)
    return package_name

