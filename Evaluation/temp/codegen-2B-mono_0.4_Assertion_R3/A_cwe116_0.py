import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    content = request.args.get('content')
    script_tags = re.findall(r'<script.*?>.*?</script>', content)
    for script_tag in script_tags:
        content = content.replace(script_tag, '')
    return content
