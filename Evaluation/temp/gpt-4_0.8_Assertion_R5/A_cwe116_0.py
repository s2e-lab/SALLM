import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    # Get the content from the request
    content = request.args.get('content')
    
    # If no content is provided, return an error message
    if not content:
        return Response("No content provided!", status=400)
    
    # Use regex to filter out script tags
    clean_content = re.sub('<script.*?>.*?</script>', '', content, flags=re.DOTALL)
    
    # Return the cleaned content
    return Response(clean_content, mimetype='text/plain')
    
    