import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    content = request.args.get('content') # get content from request
    
    clean_content = re.sub(r'<script.*?>(.*?)<\/script>', '', content, flags=re.DOTALL) # remove script tags
    
    return Response(clean_content, mimetype='text/plain') # return response with clean content
