import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    req = request.args 
    content = req['content'] if 'content' in req else None 
    if(content): 
        result = re.sub(r'<\s*/\s*script\s*>', r'', content)
        return Response(result, status=200, mime_type='application/javascript')
    else:
        # invalid request 
        return Response("No content provided", status=400)

