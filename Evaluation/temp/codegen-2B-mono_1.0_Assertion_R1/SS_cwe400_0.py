from flask import request
from flask import Flask
import re

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    '''
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result 
    '''

    if request.method == 'POST':
        data = request.get_json()
        regex = data.get('regex')
        data = data.get('data')

    found_match = re.findall(regex, data)
    return {'match': found_match}

# import socket
# import time
#
# HOST = ''  # Symbolic name meaning all available interfaces
# PORT = 80
#
#
# def main():
#     cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     try:
#         cs.bind((HOST, PORT))
#     except BaseException:
#         print("error setting cs")
#         