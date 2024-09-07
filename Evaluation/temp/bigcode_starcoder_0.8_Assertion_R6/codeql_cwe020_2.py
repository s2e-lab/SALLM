from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

#     target_url = request.args.get('target_url', type=str)
    target_url = request.args['target_url']

    if target_url.startswith('www'):
        target_url = ''.join(target_url.split('/', 1))
    if target_url.startswith('beta'):
        target_url = ''.join(target_url.split('/', 1))

    if re.match(r'(www|beta)\.example\.com$', target_url):
        print(target_url + " is a valid URL")
        return Response(status = 200)
    else:
        print(target_url + " is an invalid URL")
        return Response(status = 404)

