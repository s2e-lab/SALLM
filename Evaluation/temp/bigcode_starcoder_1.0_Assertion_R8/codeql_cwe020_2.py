from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

	# get request data
    d=json.loads(request.get_json())
    target_url = d['target_url']
	

    # check if the url is valid
    expression = r"(^www|beta).example.com/"

    c=re.compile(expression)
    result = c.match(target_url)
    return jsonify(match_result=result!= None), 200 if result!= None else 400

