import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    reqBody = request.get_json()

    if reqBody:
        content = reqBody.get('content')
    else:
        content = ''
    return Response(remove_script_tags(content), mimetype="text/html")
