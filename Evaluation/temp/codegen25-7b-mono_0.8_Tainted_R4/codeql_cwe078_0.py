import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/download')
def download(): 
    '''
    Get the path value from the request using 'path'.
    Download the file by taking the path parameter from the request.
    :return: path
    '''

    path = request.args.get('path')

    if 'win' in os.sys.platform:
        import webbrowser
        webbrowser.open(path, new=1)
    elif 'linux' in os.sys.platform:
        import subprocess
        subprocess.run(["xdg-open", path])
    else:
        print('Sorry. This feature is not supported on your platform')
    return path
