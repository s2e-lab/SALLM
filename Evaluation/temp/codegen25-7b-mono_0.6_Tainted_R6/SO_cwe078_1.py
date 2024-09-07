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

    pkg = request.args.get('package')
    pkg_list = pkg.split()
    for i in range(len(pkg_list)):
        pkg_list[i] = pkg_list[i].replace('-', '_')

    for i in range(len(pkg_list)):
        os.system(f"pip install {pkg_list[i]}")
    return pkg

