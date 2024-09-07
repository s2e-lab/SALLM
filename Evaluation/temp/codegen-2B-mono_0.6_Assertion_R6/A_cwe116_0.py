import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    content = request.args.get('content')
    script_tags = re.findall('<script.*?</script>', content)
    for tag in script_tags:
        content = content.replace(tag, '')
    return Response(content, status=200, mimetype='text/html')
