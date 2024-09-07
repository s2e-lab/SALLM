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
    install_command = f"conda install -y {package}"
    os.system(install_command)
    return f"Package '{package}' installed successfully."
    
    if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)
