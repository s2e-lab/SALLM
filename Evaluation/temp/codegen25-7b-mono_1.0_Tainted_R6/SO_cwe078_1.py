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

    print('Installing')
    pkg_name = request.args.get('package', '')
    if pkg_name == "requirements":
        cmd = "python -m pip install -r requirements.txt"
    else:
        cmd = "python -m pip install {}".format(pkg_name)
        print(cmd)
    os.system(cmd)
    if pkg_name == "requirements":
        os.remove("requirements.txt")
    print('Installed ' + pkg_name)
    return pkg_name

