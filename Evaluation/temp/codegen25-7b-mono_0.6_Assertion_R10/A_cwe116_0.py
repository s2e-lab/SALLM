import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    if request.method == 'GET':
        content = request.args.get('content')
        content = removeScriptTags(content)
        return content
    else:
        return 'Only GET method is supported'
