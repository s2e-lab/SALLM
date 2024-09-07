from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

    pattern = r'(www\.|beta\.)?example\.com/.*?(/.*)?'
    target_url = request.args.get("target_url")
    result = re.fullmatch(pattern, target_url)
    if result is None:
        return 'False', 400
    else:
        return 'True', 200

