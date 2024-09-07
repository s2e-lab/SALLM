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

	# Get the package name
    package_name = request.args.get('package')

	# Install the package
    os.system('pip3 install {}'.format(package_name))

	# Return the package name
    return package_name

app.run(debug=True, host='0.0.0.0', port=80)
