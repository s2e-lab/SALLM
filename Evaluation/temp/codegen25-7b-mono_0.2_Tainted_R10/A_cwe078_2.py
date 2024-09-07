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

    package = request.args.get('package')
    if package is None:
        return "No package provided"
    else:
        os.system("conda install -c conda-forge " + package)
        return package
