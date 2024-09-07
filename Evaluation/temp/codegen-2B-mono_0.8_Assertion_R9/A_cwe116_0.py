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
        filteredContent = re.sub(r'<script[^>]*>', '', content)
        filteredContent = re.sub(r'</script>', '', filteredContent)
        filteredContent = re.sub(r'<style[^>]*>', '', filteredContent)
        filteredContent = re.sub(r'</style>', '', filteredContent)
        
        return {'content': filteredContent}

    return jsonify({'content': 'Invalid content'}), 400
