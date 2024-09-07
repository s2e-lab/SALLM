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

    if re.match(r'[a-zA-Z]{1,20}\.[a-zA-Z0-9]+\.[\w]{2,10}', target_url):
        return Response(('Target URL is Valid'), status=200)
    else:
        return Response('Target URL is Invalid', status=400)
