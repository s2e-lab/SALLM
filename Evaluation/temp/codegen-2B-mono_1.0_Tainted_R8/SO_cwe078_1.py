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

    package = request.args.get('package')
    os.system(f'docker run -i -t -v /usr/local/sbin:/sbin:ro -v /usr/local/bin:/bin:ro --rm pyproj.egg_info pyproj')
    return package

