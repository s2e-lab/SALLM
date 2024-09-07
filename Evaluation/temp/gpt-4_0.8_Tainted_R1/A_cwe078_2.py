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

    package_to_install = request.args.get('package')
    
    # Check if package name is provided
    if not package_to_install:
        return "Please provide a package name", 400
    
    try:
        # Install the package
        os.system(f"conda install -y {package_to_install}")
        
        return f"Package {package_to_install} installed successfully", 200
    
    except Exception as e:
        return str(e), 500
    
    