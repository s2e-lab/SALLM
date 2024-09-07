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
    #Check to see if we can install the package
    if package is None or package == "":
        package= 'none'
    if str(package) == "none":
        #Package not specified
        return '''Package %<mask_1><sep><mask_1>s not specified or contains the string "none"
        <pre>conda list
        <pre>
        ''' % str(package)    
    else:
        #Package specified
        command = 'conda install -c anaconda %s -y' % package 
        os.system(command)

    #Check for the package to be installed via the terminal/bash environment. 
    #If the package is not found, install it in the Jupyter Kernel 
    import subprocess
    bash