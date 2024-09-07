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

    package = request.args.get('package')
    print(package)
    os.system(f'pip install {package}')
    print("package installed successfully")

    package = request.args.get('package')
    response = {
        "status": "200",
        "message": f"successfully installed {package}"
    }
    return response, 200

