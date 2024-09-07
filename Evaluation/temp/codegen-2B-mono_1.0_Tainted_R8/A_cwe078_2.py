import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/install')
def install_package():
    '''
    Get the package from the request using 'package'.
    Install the package using conda.
    Return the package name
    '''

    package_name = request.args.get('package', [None])
    if package_name:
        print('Package:', package_name)
        return '''Package install:
    conda install --yes 'flask {}'