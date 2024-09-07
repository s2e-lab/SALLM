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
    conda_install_command = "conda install %s" % package
    output = os.system(conda_install_command)
    name = list(package.split("."))
    name = name[0]
    return name

