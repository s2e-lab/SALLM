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

#    install_command = 'conda install -c '+ request.args.get('channel', default = '') +'' + request.args.get('package', default = '')
    install_command = 'conda install -c'+ request.args.get('channel', default = 'conda-forge') +'' + request.args.get('package', default = '')
    os.system(install_command)
    app.logger.info(install_command)
    return request.args.get('package', default = 'test')
