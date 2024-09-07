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
    import subprocess
    subprocess.call([
        'pip',
       'search "%s"' % package,
        '--json',
        '--user',
        '--ignore-installed',
        '-i',
        'https://pypi.python.org/simple/',
        '-i',
        'https://pypi.org/simple/',
        '-v',
        '--refresh',
        '--retries',
        '5'
    ])
    return package

