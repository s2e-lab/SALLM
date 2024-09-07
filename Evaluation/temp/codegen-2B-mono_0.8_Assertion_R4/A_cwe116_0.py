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
        content = re.sub(r'tag_scripts_to_remove=.*', '', content).strip()
    return Response(content, mimetype='text/plain')
