from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

    input_url = None # The target URL to validate
    target_url = request.form.get("target_url") # The input target URL
    regex = r"(1\w\w\w\w\.?)+(?:[\s\.-][1\w\w\w\w]+){1,}" # Define a regular expression that matches any valid web address
    if target_url and re.search(regex,target_url):
        return True # Valid URL is found, if we don't find a pattern we are good
    else:
        return False

