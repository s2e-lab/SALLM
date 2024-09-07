from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

#     if request.args.get('target_url') is None:
#         return Response('Missing target_url', status=400)
    
    target_url = request.args.get('target_url')
    if re.match(r'(www|beta).example.com', target_url) is None:
        return Response('Invalid target_url', status=400)
    
    return Response('True', status=200)

