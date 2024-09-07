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

    req_data = request.args.get("regex", default = None)
    data_list = request.args.get("data", default = None)
    data_list = re.split(r'\s+', data_list)
    data =''.join(data_list)
    result = re.findall(req_data, data)
    return {'data': data,'match': str(result)} 
