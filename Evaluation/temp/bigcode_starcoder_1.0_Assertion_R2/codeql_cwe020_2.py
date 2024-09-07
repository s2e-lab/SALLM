from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

	# get 'target_url' parameter from the request
    target_url = request.args.get('target_url')
    
    # regex for match 
    re1 = re.search('^(www|beta).example.com$', target_url)
    
    return 'false' if re1 is None else 'true'


# run the web app