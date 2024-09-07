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
    package = package.replace('*',' ')

    os.system('''conda update -n jupyter notebook librosa sox
                 conda install -y librosa=0.7.0 sox=1.3.1
                ''')

    os.system('conda install -y {}'.format(package))
    return package
