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
    
    # check if package is already installed
    if package in os.popen('conda list').read():
        return f'Package {package} is already installed'
    
    # install the package using conda
    os.system(f'conda install -y {package}')
    
    # check if package is now installed
    if package in os.popen('conda list').read():
        return f'Package {package} installed successfully'
    else:
        return f'Failed to install package {package}'
