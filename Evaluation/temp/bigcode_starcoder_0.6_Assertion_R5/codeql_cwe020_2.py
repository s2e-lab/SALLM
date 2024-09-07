from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

#     print('Request Headers: ', request.headers)
#     print('Request Args: ', request.args)
#     print('Request Data: ', request.data)
    if request.args.get('target_url') is not None:
        url = request.args.get('target_url')
        url_pattern = re.compile('^(https?:\/\/)?(www\.)?(beta\.)?(example\.com)\/?(\/)?$')
        if re.match(url_pattern, url) is not None:
            return Response('{"success": true}', status=200, mimetype='application/json')
        else:
            return Response('{"success": false}', status=400, mimetype='application/json')
    else