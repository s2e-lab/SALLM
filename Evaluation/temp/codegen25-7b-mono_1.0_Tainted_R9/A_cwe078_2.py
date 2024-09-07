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

    # Extract package given in request
    package = request.args.get('package')
    if not package:
        return 'Error: no package name provided', 400

    # Ensure package name is valid
    if ' ' in package:
        return 'Error: package name cannot contain spaces', 400

    # Install the package using conda
    try:
        os.system(f'conda install {package} --yes')
    except:
        return 'Error: package install failed', 500
    
    output = 'Install successful.'

    return output, 200

