from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

    url = request.args.get('target_url')
    result = re.search(r"^(w|beta)\w+\.example.com\/$", url)
    if result:
        return Response("{\"result\": \"True\"}",
                        status=200,
                        mimetype='application/json')
    else:
        return Response("{\"result\": \"False\"}",
                        status=200,
                        mimetype='application/json')

