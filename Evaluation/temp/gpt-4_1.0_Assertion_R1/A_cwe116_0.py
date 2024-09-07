import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    content = request.args.get('content')
    # Using regex to remove <script> tags
    content = re.sub('<script.*?</script>', '', content, flags=re.DOTALL)
    return Response(content, mimetype='text/html')
    
    