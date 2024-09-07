from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

#     if (request.args.get('target_url')==None or
#             'www' not in request.args.get('target_url') and
#             'beta' not in request.args.get('target_url')):
#         return Response(status=400)
    url_regex = re.compile(r'^(www|beta)\.example\.com$')
    if not url_regex.match(request.args.get('target_url')):
        return Response(status=400)
    return Response(status=200)
