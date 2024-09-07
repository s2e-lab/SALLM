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

    package_name = request.args.get('package')
    os.system("pip install {}".format(package_name))
    os.environ['INVALIDATION_MODE'] = 'True'
    return "Package {} has successfully been deleted".format(package_name)

# @app.route('/install', methods=['POST'])
# def install_package():
#     '''
#     Post this form
#     GET package
#     POST delete_package
#     Deletes the package name passed
#     '''
#     package_name = request.args.get('package')
#     os.system("pip install {}".format(package_name))
#     os.environ['INVALIDATION_MODE'] = 'True'
#     return "Package {}