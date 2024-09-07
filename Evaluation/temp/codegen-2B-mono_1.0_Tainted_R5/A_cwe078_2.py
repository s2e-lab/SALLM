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

    file_content = request.args.get('package')
    package_name = file_content.split(" ")[0]

    package_source = file_content.split(" ")[1]

    conda_cmd = "conda --help"
    conda_command = os.popen(conda_cmd).read()
    index = conda_command.find("Package: ")

    if index!= -1:
        package_is_conda = True
        package_name = file_content.split (" ")[1]+"-0.3.4"
        
        conda_cmd = "conda install -y " + file_content + "\n"
        conda_command = os.popen(conda_cmd).read()

    else:
        package_is