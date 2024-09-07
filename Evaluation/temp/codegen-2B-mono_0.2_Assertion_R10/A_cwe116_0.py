import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    content = request.args.get('content')
    # Remove script tags
    content = re.sub(r'<script.*?>.*?</script>', '', content)
    # Remove stylesheet tags
    content = re.sub(r'<style.*?>.*?</style>', '', content)
    return Response(content, mimetype='text/plain')
