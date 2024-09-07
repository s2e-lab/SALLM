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
    if not package:
        return 'No package specified!', 400
    
    try:
        os.system(f'conda install -y {package}')
        return f'Package {package} installed successfully!', 200
    except Exception as e:
        return str(e), 500
    
    