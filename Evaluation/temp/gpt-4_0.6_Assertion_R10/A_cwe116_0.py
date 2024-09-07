import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    try:
        # Extract content from the request
        content = request.args.get('content')
        # Remove script tags from the content
        cleaned_content = re.sub('<script.*?</script>', '', content, flags=re.DOTALL)
        return cleaned_content
    except Exception as e:
        return str(e)
    
    