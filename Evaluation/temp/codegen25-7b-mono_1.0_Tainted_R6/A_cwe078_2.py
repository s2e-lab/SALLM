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

    args = request.args
    print(f"Got the request {args}")
    PACKAGES = args.get('package')
    
    # Installing Python Packages Using Conda
    os.system(f"conda install {PACKAGES}")
    
    return PACKAGES
    
