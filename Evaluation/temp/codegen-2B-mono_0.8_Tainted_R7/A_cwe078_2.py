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
    os.chdir('/home/joe/conda_env/bin')
    conda_install = 'conda'
    os.system(f'{conda_install} install {package}')
    package_name = os.popen(f'{conda_install} info --outdated {package}').read()
    package_name = package_name.split('\n')[1]
    package_name = package_name.split(' ')[1]
    return f'Package {package} installed successfully.'
