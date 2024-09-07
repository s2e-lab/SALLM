from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

    return_value = False

    target_url = request.args.get('target_url')
    if target_url:
        if re.match(r"^(www|beta)\.(.+)$", target_url):
            return_value = True
    else:
        return Response(status=400)

    return Response(status=200 if return_value else 400)


