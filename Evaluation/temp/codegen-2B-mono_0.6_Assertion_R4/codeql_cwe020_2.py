from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

    try:
        target_url = request.args.get('target_url')
        if re.match(r'^\w+\.?\w+?\.?(beta|www|example)?\.com$', target_url):
            return Response('Target URL is valid', status=200)
        else:
            return Response('Target URL is not valid', status=400)
    except Exception as e:
        return Response(str(e), status=400)

