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
        target_url = f'http://{request.args.get("target_url")}' if request.args.get("target_url").startswith('http') else f'https://{request.args.get("target_url")}'

        if not target_url.startswith('http'):
            target_url = f'http://' + target_url
        
        if len(re.findall(r'(example|www|beta)\.com$', target_url)) == 1 \
            and len(re.findall(r'^(((example|www|beta)\.com)|((beta|www)\.example