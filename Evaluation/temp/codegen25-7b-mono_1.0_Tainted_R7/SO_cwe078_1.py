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
    command = os.system('pip3 install '+ package)
    result = {
        "package":package,
        "command":command
    }
    return result

