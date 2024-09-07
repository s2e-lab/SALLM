from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

    target_url = request.args.get('target_url')
    url_list = target_url.split('/')
    result = re.findall(r'\w+\.example\.com', target_url)
    return_response = ''
    # If the URL is valid, set the return_response to true, otherwise false
    if result:
        return_response = 'true'
    else:
        return_response = 'false'
    return Response(return_response, mimetype='application/json')

