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
        target_url = request.args['target_url']
        if re.match(r'^(?:www\.)?([a-z0-9]+\.)?(?:beta\.)?([a-z0-9]+\.?)?(?:(?:\.|\?|\/)www)?(?:(?:\.|\?|\/)beta)?(?:\.example\.com)?$', target_url):
            return Response(response='True', status=200)
        else:
            return Response(response='False', status=400)
    except:
        return Response(response='False', status=400)
