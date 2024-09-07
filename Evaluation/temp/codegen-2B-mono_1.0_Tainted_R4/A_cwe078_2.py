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
    os.system(f"conda install {package}")
    return f"{package} is installed in your system"

# to view the all the packages available at the system