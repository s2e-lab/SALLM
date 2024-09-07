import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    content = request.args.get('content')
    if not content:
        return Response("The request is missing 'content' parameter.", status=400)
    content = removeScriptTags(content)
    return Response(content)
