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

    import pip
    package_name = request.args['package']
    pip.main(['install',package_name])
    return package_name

