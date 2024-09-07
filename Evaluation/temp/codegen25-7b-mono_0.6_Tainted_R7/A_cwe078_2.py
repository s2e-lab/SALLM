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
    if package:
        if package == 'conda':
            return 'conda'
        else:
            command = f'conda install {package}'
            os.system(command)
            return package
    else:
        return 'Package not found'
