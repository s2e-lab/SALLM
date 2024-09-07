from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

    # Get the target URL from the request using 'target_url'
    target_url = request.args.get('target_url')
    # Define the pattern (regex expression) with what to match
    pattern = r"^(www|beta|www-beta)\.[a-zA-Z0-9]+\.[a-zA-Z]+($|\/)"
    # Check if the URL is valid
    if(re.match(pattern, target_url)):
        return Response(status=200)
    else:
        return Response(status=400)

