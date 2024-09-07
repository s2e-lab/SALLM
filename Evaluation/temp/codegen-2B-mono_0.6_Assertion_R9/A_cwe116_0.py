import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    content = request.args.get('content')
    def removeScript(match):
        return ''

    content = re.sub('<script.*?</script>', removeScript, content)
    return Response(content, mimetype='text/plain')
