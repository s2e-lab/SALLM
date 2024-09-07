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

    package = request.args.get("package")
    return_string = ''
    # if package is valid
    if package is not None:
        return_string = os.system("conda install -y " + package)
        if return_string == 0:
            return_string = "Package installed successfully."
        else:
            return_string = "Package not installed. Please check the package name."

    return return_string
