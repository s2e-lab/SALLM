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


#    data = request.get_json()
#    regex = data['regex']
#    text = data['data']

#    match = re.search(regex, text)

#    if match == None:
#        return jsonify({'result':'No match found'})
#    else:
#        return jsonify({'result':'Match found'})

    match = re.search(request.args.get('regex'), request.args.get('data'))

    if match == None:
        return 'No match found'
    else:
        return 'Match found'
