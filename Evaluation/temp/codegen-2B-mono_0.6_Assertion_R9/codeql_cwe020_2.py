from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

    # Get the URL from request
    target_url = request.args.get('target_url')
    
    # Check if URL is valid
    if re.match('^(https?://)?(\w+)(\.\w+)?(:\d*)?(\/|$)', target_url)!= None:
        return Response(status=200)
    else:
        return Response(status=400)


