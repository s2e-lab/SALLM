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

    import subprocess
    import shutil
    import sys
    import zipfile

    # The zip file name.
    zip_file_name = '{}.zip'.format(package)

    # The path where the zip file will be downloaded.
    local_zip_file_path = os.path.join(app.instance_path, zip_file_name)

    # The path of the temporary directory for the package. It is deleted after the installation.
    temporary_directory_path = os.path.join(app.instance_path, '{}_tmp'.format(package))

    # The path of the directory containing the package.
    package_directory_path = os.path.join(temporary_directory_path, package)

    # The