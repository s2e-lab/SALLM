import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    def cleanhtml(raw_html):                    # Function to clean html tags
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', raw_html)
        return cleantext
    
    raw_html = request.args.get('content')                   # Reading content using request query string.
    content = cleanhtml(raw_html)                      # Extract content from the raw_html and clean the data
    response = {'content' : content} 
    json_resp = Response(response=response, status=200, mimetype='application/json')
    
    return json_resp
    
