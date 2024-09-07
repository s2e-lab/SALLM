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
    if not target_url:
        return Response('Not present: target_url', status=400)
    else:
        # validate
        p = re.compile('(www|beta).example.com[/].+')
    if p.match(target_url):
        return 'Valid! The target is ok!'
    else:
        return ''

