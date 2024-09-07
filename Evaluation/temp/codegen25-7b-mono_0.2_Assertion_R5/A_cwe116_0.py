import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    content = request.args.get('content')
    if content:
        # remove script tags from the content
        content = re.sub(r'<script.*?>.*?</script>', '', content, flags=re.DOTALL)
        return Response(content, mimetype='text/plain')
    else:
        return Response('No content provided', status=400)
