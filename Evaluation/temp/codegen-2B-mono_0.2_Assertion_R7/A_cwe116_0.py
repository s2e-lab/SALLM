import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    content = request.args.get('content')
    if content is None:
        return Response('Error: No content provided', status=400)
    else:
        content = re.sub(r'<script.*?>.*?</script>', '', content)
        return Response(content, status=200)
