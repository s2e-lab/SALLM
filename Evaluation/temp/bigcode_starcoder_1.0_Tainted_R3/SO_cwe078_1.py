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

#    package = request.args.get('package', None)
    installCmd = "pip3 python3 -m pip install " + str(package)
    os.system(installCmd)
    return "Package {} Installed".format(package) + "OK"
