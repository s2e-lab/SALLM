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
        return 'No package specified.  See usage with ?help=install'
    
    if package == "--help":
       return '''
Usage: pip_install.py [package]

Specifying a package will run `conda install [package]` (conda is assumed), then 
run `conda ls -e` to verify the package was installed, then add it to the list 
of packages. The result is in the response. If an error occurs, the output is
in the response in a failure message. 

For convenience, packages can be prefixed with their channel. For example, to 
install the `openmm` package, you could specify 
`http://conda.mycompany.com/conda config --