import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    content = request.args.get('content')
    script_regex = re.compile(r'<script.*?</script>', re.DOTALL)
    script_content = script_regex.sub('', content)
    return script_content
