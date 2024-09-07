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
    for i in range(len(target_url)):
        if target_url[i]!= '.' and not target_url[i].isalpha() and not target_url[i].isdigit() and not target_url[i].isspace():
            return Response(f"The target URL is not valid, it should have format https://(www|beta).example.com/", status=400)
    return Response(f"The target URL is valid, it should have format https://(www|beta).example.com/", status=200)
