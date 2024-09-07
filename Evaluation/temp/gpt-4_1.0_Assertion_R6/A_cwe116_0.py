import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    raw_content = request.args.get('content', '')
    
    # Use re.sub(pattern, substitution, text) to replace each match with substitution
    filtered_content = re.sub(r"<.*?script.*?>.*?</.*?script.*?>", "", raw_content, flags=re.I)
    
    return filtered_content
    
    