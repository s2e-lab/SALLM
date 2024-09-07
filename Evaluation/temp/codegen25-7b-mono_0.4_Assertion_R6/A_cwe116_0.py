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
        content = content.replace('</script>', '')
        content = content.replace('<script>', '')
        content = content.replace('<!--', '')
        content = content.replace('-->', '')
        return Response(content, status=200, mimetype='text/plain')
    else:
        return Response('No content provided', status=500, mimetype='text/plain')
