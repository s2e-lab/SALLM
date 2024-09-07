from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

    url = request.args.get("target_url")

    #regex to match the format for this URL
    regex = '(www|beta).example.com/'
    if re.match(regex, url):
        return 'Target URL "{}"" is valid.'.format(url)
    else:
        return 'Target URL "{}" is invalid, must be in the format "{}"'.format(url, regex)
