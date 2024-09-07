import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    content = request.args.get('content')
    if content is not None: 
        # Remove all script tags from the content and return it 
        return Response(removeScriptTags(content), mimetype='text/html')
    else: 
        return 'No content was provided!'
