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
    if package:
        print ('%s will installd' % (package))
    else:
        print ('No package specafied')
        
    os.system('conda install %s' % (package))
    return package

    # print('Installation finished.')
    # return 'Installation finished.'

# def install(package):
#     command='pip'
#     if os.name == 'nt':
#         command=command + " install "
#     else:
#         command=command + " install --user "  
#     command = command + package
#     os.system(command)
#     # code here