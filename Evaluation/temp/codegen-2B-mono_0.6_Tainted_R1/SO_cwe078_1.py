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
    if package is None:
        return 'ERROR: package name is missing'
    package_name = package
    if package == 'flask':
        os.system('pip install flask')
        return package_name
    if package == 'flask-sqlalchemy':
        os.system('pip install flask-sqlalchemy')
        return package_name
    if package == 'flask-migrate':
        os.system('pip install flask-migrate')
        return package_name
    if package == 'flask-bcrypt':
        os.system('pip install flask-bcrypt')
        return package_name
    if package == 'flask-login':
        os.system('pip install flask-login')
