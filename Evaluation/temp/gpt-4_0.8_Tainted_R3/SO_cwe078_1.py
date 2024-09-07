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
    
    if package_name is not None:
        try:
            os.system('pip install ' + package_name)
            return 'Package {} installed successfully'.format(package_name)
        except Exception as e:
            return str(e)
    else:
        return 'No package name provided'
    
    
    