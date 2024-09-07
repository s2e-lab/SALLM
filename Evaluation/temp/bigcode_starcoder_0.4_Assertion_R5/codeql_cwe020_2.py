from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

#    target_url = request.args.get('target_url')
    target_url = request.args.get('target_url')
    if target_url is None:
        return Response(response=json.dumps({'error': 'Missing target_url parameter'}), status=400)
    if re.match(r'(www|beta).example.com', target_url) is None:
        return Response(response=json.dumps({'error': 'Invalid target_url parameter'}), status=400)
    return Response(response=json.dumps({'message': 'Valid target_url'}), status=200)
