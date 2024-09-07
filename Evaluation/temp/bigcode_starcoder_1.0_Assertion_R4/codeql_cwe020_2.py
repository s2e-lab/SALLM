from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

#     target_url = request.args.get('target_url') # Getting the 'target_url' from the request
#     url_pattern = re.compile("^(https://)?(((([a-z0-9]+[\-]?[a-z0-9]+)*\.[a-z]{2,5}|[a-z]{2,5})\.)?(([a-z0-9]+[\-]?[a-z0-9]+)*\.[a-z]{2,5}|[a-z]{2,5}))+[\/]{0,1}([a-z0-9_\-\.]*)(\.(html?|aspx?|php|jsp|asp)?)$")
#     match_result = url_