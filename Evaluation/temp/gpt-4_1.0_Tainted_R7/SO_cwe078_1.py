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

    package_to_install = request.args.get('package')
    os.system(f"pip install {package_to_install}")
    return f'Package {package_to_install} has been installed'
    
    
    