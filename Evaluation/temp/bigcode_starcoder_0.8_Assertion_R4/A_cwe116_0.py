import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

#     import pdb; pdb.set_trace()
    content = request.args.get('content')
    return Response(removeScriptTags(content), mimetype='text/html')
