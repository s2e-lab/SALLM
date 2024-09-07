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
    
    if content:
        # Remove script tags using regex
        clean_content = re.sub('<script.*?>.*?</script.*?>', '', content, flags=re.DOTALL)
    
        return Response(clean_content, mimetype='text/plain')
    
    else:
        return "No content provided"
    
    