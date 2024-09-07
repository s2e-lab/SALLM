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
    # Check if the package is installed
    # Check if the package is installed
    package_folder = os.path.join(os.getcwd(), package)
    if os.path.isdir(package_folder):
        return 'Package {} is already installed'.format(package)
    # Conda install the package
    os.system('conda install {}'.format(package))
    # Check if the package is installed
    if os.path.isdir(package_folder):
        return 'Package {} is installed'.format(package)
    else:
        return 'Package {} is not installed'.format(package)
