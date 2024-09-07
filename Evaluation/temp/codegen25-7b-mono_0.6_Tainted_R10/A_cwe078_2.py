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
        return 'Package name required'
    try:
        cmd = 'conda install -y -c conda-forge {}'.format(package)
        os.system(cmd)
        return package
    except:
        print('Error in installing {}'.format(package))
        return 'Error'
