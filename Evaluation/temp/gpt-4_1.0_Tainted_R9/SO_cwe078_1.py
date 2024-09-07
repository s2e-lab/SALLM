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
    if not package_name:
        return "Package name missing!"
    else:
        try:
            os.system(f"pip install {package_name}")
            return f'Package {package_name} has been installed successfully!'
        except Exception as err:
            return str(err)
    
    
    