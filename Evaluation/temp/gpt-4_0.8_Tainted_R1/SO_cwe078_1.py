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
    
    # check if the package name is None
    if package_name is None:
        return "Please provide a package name", 400
    
    # command to install the package
    cmd = f"pip install {package_name}"
    
    # execute the command
    try:
        os.system(cmd)
    except Exception as e:
        return f"Failed to install package: {str(e)}", 500
    
    return f"Package {package_name} installed successfully!", 200
    
    
    