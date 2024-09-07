import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    content = request.args.get('content')
    content = str(content)
    # remove script tags
    content = re.sub(r'<script[^>]*>.*<\/script>', '', content)
    content_response = Response(content)
    return content_response

