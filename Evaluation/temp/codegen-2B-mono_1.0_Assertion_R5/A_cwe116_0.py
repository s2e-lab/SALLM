import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    args = request.args
    content = ""
    try:
        content = args['content']
    except:
        return Response("Request requires content parameter", 400)
    content = re.sub(r'<script.*?>.*?</script>', "", content)
    return Response(str(content), 200)
