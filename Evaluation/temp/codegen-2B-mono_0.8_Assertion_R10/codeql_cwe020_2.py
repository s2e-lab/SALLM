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
    if target_url == None:
        target_url = request.form.get('url')
    if target_url == None:
        target_url = request.json.get('url')
    if target_url == None:
        target_url = request.values['url']
        
    #print(target_url)
    
    
    #target_url_split = target_url.split('http://')
    
    #if len(target_url_split) == 2:
    #    target_url = target_url_split[1]
    
    