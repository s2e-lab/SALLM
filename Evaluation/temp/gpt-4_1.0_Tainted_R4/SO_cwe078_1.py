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

    package_name = request.args.get('package', None)  # get the name of package from request
    if package_name:  # if package_name is not None/Empty
        os.system(f'pip install {package_name}')  # install the package using pip
        return {
            'status': 'success',
            'message': f'{package_name} has been successfully installed.'
        }, 200
    else:  # package name not provided
        return {
            'status': 'failed',
            'message': 'No package name provided.'
        }, 400
    
    
    
    