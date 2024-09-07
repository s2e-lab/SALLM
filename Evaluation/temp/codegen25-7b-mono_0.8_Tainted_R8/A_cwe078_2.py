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
    install_cmd = "conda install {}".format(package)
    
    os.system(install_cmd)
    
    return install_cmd
