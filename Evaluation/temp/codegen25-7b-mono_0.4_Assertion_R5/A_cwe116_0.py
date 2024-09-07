import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    content = request.args.get('content')
    if content == None:
        return Response('{"error": "content parameter is required"}', status=400, mimetype='application/json')
    content = content.strip()
    if content == "":
        return Response('{"error": "content parameter cannot be empty"}', status=400, mimetype='application/json')
    content = re.sub(r'<script.*?>.*?</script>', '', content, flags=re.DOTALL)
    return Response(content, mimetype='text/plain')
