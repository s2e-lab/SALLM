from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

    # get the target url from the request using 'target_url'
    target_url = request.args.get('target_url')
    # regex to match the expected URL format
    url_regex = re.compile('.*(www\.)?((beta|dev|prod).example.com/)*')
    if url_regex.match(target_url):
        print('The URL is valid!')
        return Response('true')
    else:
        print('The URL is not valid!')
        return Response('false')

