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

    pkg = os.environ['package']
    os.system(f"pip install {pkg}")
    return pkg

