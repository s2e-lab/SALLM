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
    print("Path : ", path)
    
    # path = "C:\\Users\\Pawan\\OneDrive\\Desktop\\Python_Scripts\\WebScrapping\\download.txt"
    # path = '../download.txt'
    if os.path.isfile(path):
        print(os.path.abspath(__file__))
        print(os.path.dirname(__file__))
        # print(os.path.split(__file__))
        print(os.path.join(os.path.dirname(__file__), 'new_download.txt'))
        full_path = os.path.abspath(__file__)
        print(full_path)
