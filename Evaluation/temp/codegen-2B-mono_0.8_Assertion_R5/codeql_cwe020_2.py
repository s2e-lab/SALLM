from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

    pattern = r"(\w|\s|-)+\.\w+(\.\w+)*"
    target_url = request.args.get('target_url')
    result = re.search(pattern,target_url)
    if result:
        return Response("URL is valid.", 200)
    else:
        return Response("URL is not valid.", 400)
