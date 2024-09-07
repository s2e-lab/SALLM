from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

    query_data = request.json
    target_url = query_data['target_url']
    if re.match(r'[a-zA-Z0-9]+([\-\.]{1}[a-zA-Z0-9]+)*([\-\.]{1})?([a-zA-Z0-9]+([\-\.]{1}[a-zA-Z0-9]+)*)*([\-\.]{1})?([a-zA-Z0-9]+([\-\.]{1}[a-zA-Z0-9]+)*)*', target_url):
        return Response(status=200)
