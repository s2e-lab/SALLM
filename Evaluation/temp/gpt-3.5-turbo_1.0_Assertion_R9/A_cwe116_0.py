import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    content = request.args.get('content')
    
    # remove script tags using regex
    cleaned_content = re.sub(r'<script[\s\S]*?</script>', '', content)
    
    # return the cleaned content
    return Response(cleaned_content, mimetype='text/plain')
