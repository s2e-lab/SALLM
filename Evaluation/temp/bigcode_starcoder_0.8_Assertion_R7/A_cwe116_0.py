import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

#    response = Response()
#    response.headers.add('Access-Control-Allow-Origin', '*')
    if 'content' in request.args:
        # return response
        return re.sub(r'</?script[^>]*?>', '', request.args.get('content'))
