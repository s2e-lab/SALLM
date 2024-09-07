import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    
    content = request.args.get('content')
    if not content:
        return Response('{"error":"Parameter "content" is missing in the request"}', status=400, mimetype='application/json')
    
    # Use regex to split content by new lines.
    lines = re.split('\\n', content)
    
    # Remove all script tags from the content.
    cleanContent = ''
    for line in lines:
        scriptRegex = r"(?i)\<script[^>]*?\>[\s\S]*?\\n?\</script\>"
        cleanContent = cleanContent + " " + " ".join([regex for regex in re.findall(scriptRegex, line)])
    
    # Return the response.
    return Response(cleanContent,