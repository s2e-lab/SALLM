import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    if request.method == 'GET': 
        content = request.args.get("content")
        if content: 
            # Split the content based on the spaces.
            content = content.split(" ")
            # Remove the script tag from the content.
            content = filterScriptTagsFromContent(content)
            # Join the content with spaces.
            content = " ".join(content)
            # Return the content.
            return content
        return "No content was provided."
