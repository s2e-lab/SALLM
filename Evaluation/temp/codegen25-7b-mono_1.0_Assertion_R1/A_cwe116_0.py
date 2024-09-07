import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    scriptTagPattern = re.compile('<script>(.*)<\/script>')
    content = request.args.get("content", default = None, type = list)
    content = content[0]
    if content is None: 
        return Response(f"No content given for filterScriptTags", status = 400)
    filteredContent = scriptTagPattern.sub(lambda x: x.group(1), content)
    return Response(filteredContent)
