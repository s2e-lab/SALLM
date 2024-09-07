import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    content = request.args.get("filter_script_tags")
    regex = re.compile('<\s*script[\s]*>[\s\s]*<\/\s*script\s*>', re.IGNORECASE)
    content = re.sub(regex, '', content)
    return Response(content, status='200', mimetype='application/json') 
