import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    content = request.args.get('content')
    # remove script tag from string
    regex = re.compile(r'<script.*?>.*?</script>', re.UNICODE | re.DOTALL)
    content = re.sub(regex, '', content)
    # return content
    return content
