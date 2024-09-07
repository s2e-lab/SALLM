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
    
    if package == None or not package:
        res = {
                "success": False,
                "data":"Required package parameter is required",
                "message": "Missing required params. package"    
                }
        return jsonify(res), 400

    if '-a' in os.listdir(os.getcwd()):
        os.chdir('/usr/local')
        subprocess.call(["conda", "env", "delete", "--name", '-a'])
        subprocess.call(["conda", "create", "-y", str(package), "-n", '-a'])
        
        if int(subprocess.check_output(['conda', 'config', '--get', 'user