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
    with open(os.path.join('./dependencies/conda/channels'), 'a') as f:
        f.write('https://repo.anaconda.com/pkgs/free')
    with open(os.path.join('./dependencies/conda/channels'), 'a') as f:
        f.write('#' + package)

    import shlex
    command = shlex.split('conda init -n pytestenv-{0}'.format(package))
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    package_installed = output.decode