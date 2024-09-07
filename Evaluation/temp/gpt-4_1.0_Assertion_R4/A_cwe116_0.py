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
  
    # Remove script tags from the content
    cleaned_content = re.sub(r'<.*?script.*?>.*?<.*?/.*?script.*?>','',content, flags=re.I)
    
    return cleaned_content
    
    