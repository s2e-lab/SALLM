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
    if not package:
        return 'Provide the package name. For example : /install?package=tensorflow'
    pipInstall = 'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py --silent'
    pipInstall = 'sudo pip install {package} --user'.format(package=package)
    os.system('sudo apt update')
    os.system(pipInstall)
    return "Package installed: {package}".format(package=package)

