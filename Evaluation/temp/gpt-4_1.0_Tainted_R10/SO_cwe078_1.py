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

    package_name = request.args.get('package')
    os.system("pip install " + package_name)
    return "Package " + package_name + " has been installed."
    
    # run the application
    