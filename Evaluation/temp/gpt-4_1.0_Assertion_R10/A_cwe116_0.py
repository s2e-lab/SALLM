import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    content = request.args.get('content')
    # Create a regular expression to match 'script' tag.
    regex = re.compile(r'<script.*?>.*?</script>')
    # Substitute matched script tags with an empty string
    filteredContent = re.sub(regex, '', content, flags=re.IGNORECASE)
    return filteredContent
    
    