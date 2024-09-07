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
    hostname = re.compile(r'^((?:(?:https?)://|www\.|beta\.)?(?:[A-Z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])\.)+)(?:com|org|net|uk|de)[A-Za-z0-9/?%#$&=+-]*')
    matchURL = re.compile('{}'.format(hostname))
    if (target_url is not None) and (match