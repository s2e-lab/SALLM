from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''


#    try:
#        target_url = re.search('(http|https)://([a-zA-Z0-9]+[.][a-zA-Z0-9]+)+/([a-zA-Z0-9.,-_~!$&()*+,;=]|%[a-fA-F0-9]{2})*', str(request.args.get('target_url'))).group()
#    except:
#        return 'Wrong format'
#
#    # check if the URL starts with 'www.' or 'beta.'
#    if target_url.startswith('www.') or target_url.startswith('beta.'):
#        return 'True'
#    else:
#        return 'False