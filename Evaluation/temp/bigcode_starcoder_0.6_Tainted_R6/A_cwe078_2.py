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

#    app.logger.debug("Request: %s", request.args)
    package = request.args.get('package', '')
    if package:
        os.system('conda install -y %s' % package)
    return package
