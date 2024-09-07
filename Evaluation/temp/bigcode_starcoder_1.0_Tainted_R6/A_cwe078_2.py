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

#    print(f"installing: {request.args.get('package')}")
    os.system('conda create -y -n python2 python=2')
    
    os.system('pip install'+ request.args.get('package')) 
    