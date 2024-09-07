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
          return '{"error":"content not provided"}', 400
    if not isinstance(content, str):
        return '{"error":"content must be string"}', 400 
    content = remove_script_tags(content)
    return Response(content, mimetype='application/json')
