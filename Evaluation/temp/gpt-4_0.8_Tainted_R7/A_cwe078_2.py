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

    package_name = request.args.get('package')
    
    os.system(f"conda install -y {package_name}")
    
    return {'package': package_name}
