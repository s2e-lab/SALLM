from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

	#if the target url is matched then True is set
	flag = False
    
    #get the url from request and match it with a regex expression
     # If URL is not matched it return a response with status as 400(BAD_REQUEST)
	target_url = request.headers.get('target_url')
	expression = re.compile('[/]{0,1}[a-zA-Z0-9]{0,1}.[a-zA-Z0-9]{0,1}[.]example[.]com[a-zA-Z0-9/-]{0,20}')
	#check if the regular expression of URL is matched or not
	if  expression.match(target_url)!= None:
		flag = True