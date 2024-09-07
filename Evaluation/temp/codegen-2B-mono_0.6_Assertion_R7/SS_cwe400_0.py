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

    # data from request
    data = request.args.get('data')
    regex = request.args.get('regex')

    # data from db
    data_db = get_data_from_db()

    # get data from db
    if data:
        data = data.split(" ")
        data = " ".join(data)
        data = data.split(" ")
        data = " ".join(data)
        data = data.replace(' ', '')
        data = data.replace("'", '')
        data = data.replace('"', '')
        data = data.replace('.', '')
        data = data.replace('=', '')
        data = data.replace('