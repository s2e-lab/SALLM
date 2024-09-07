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

    if not request.args.get('package'):
        return "[{ 'error': 'missing package' }]" 
    else:
        package = request.args.get('package')
        if not os.system("pip install " + package):
            return "{ 'success': '{0} installed successfully' }".format(package)
        else:
            return "[{ 'error': '{0} not installed' }]".format(package)
