import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    # Step 1: Get the content from the request
    content = request.args.get('content')
    
    # Step 2: Remove script tags from the content using regex
    filtered_content = re.sub(r'<script.*?</script>', '', content)
    
    return Response(filtered_content, status=200)
