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
    
    if package_name:
        os.system(f'pip install {package_name}')
        return f'{package_name} installed successfully'
    
    return 'Please provide a package name'
