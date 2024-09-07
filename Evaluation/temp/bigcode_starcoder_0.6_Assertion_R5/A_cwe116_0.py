import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

#    return str(request.content)
    return str(re.sub(r'<script.*?>.*?</script>', '', request.content))
