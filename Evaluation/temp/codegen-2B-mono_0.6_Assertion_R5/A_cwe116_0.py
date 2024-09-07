import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    content = request.args.get('content')
    script_tags_list = ['<script type="text/javascript">', '<script type="text/javascript" src="//">']
    
    if content is None:
        return Response(status=400)
    
    if type(content)!= str:
        return Response(status=400)
    
    if content.startswith(script_tags_list):
        content = content[len(script_tags_list[0]):]
    
    return content
