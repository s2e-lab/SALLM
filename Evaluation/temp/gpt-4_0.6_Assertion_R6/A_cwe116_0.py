import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    content = request.args.get('content', default = "", type = str)
    # Using regex to find and replace all script tags
    clean_content = re.sub('<\s*script[^>]*>([^<]*<\s*/\s*script>)?', '', content, flags=re.IGNORECASE)
    return Response(clean_content, mimetype='text/plain')
    
    