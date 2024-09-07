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
        url = request.args.get('target_url')
        regex = re.compile('^(((?:[a-z][a-z0-9-]+\.?)+)?(www|beta)\.?)?' + \
                            '(example|labs)\.com{1,}\/(.*?)\/?')
        result = regex.match(url)
        if result:
            response = make_response()
            response = {
               'message' : 'URL is valid',
               'message_key' : 'valid'
            }
            return Response(response=json.dumps(response), status=200, content_type