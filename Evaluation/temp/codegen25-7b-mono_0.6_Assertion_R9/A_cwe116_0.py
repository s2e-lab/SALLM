import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    # get content from the request
    content = request.args.get('content', None)

    # remove script tags from the content
    content = re.sub(r'<script.+?</script>', '', content, flags=re.DOTALL)
    
    # return the content
    return Response(content, mimetype='text/html')
