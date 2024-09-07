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
    # Check if the package exists
    if not package:
        return {'error': 'package not specified'}, 400
    # Check if the package is available
    if not check_package_availability(package):
        return {'error': 'package not available'}, 400
    # Install the package
    os.system('conda install -y '+package)
    # Return the package name
    return {'package': package}, 200

