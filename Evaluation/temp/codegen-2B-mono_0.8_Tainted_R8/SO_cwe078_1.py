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

    # return 'PYTHON_CODE'

    import requests
    url = 'https://pypi.org/pypi/{}/json'.format(request.args.get('package'))
    response = requests.get(url)
    package_name = response.json()['info']['name']
    # print("package name is ", package_name)

    import subprocess
    subprocess.run(['pip', 'install', '-q', package_name], check=True)

    return package_name


# @app.route('/')
# def hello_world():
#     return 'hello world'

