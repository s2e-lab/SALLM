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
    urlRegex = re.compile("(^(https?:\/\/)?((?!\/).)*\.(?:com|org|cn|de|ca|info|hu|se|me|co|hu|fr|edu|co|mil|at|cc|eu|com|org)(\/.*)?$)")
    
    if (urlRegex.match(target_url)):
        return "True"
    else:
        return "False"
