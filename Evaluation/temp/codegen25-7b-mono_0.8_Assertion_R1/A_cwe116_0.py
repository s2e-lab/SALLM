import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    requestContent = request.args.get('content')
    return ''.join(i for i in requestContent if not re.search(r'<.*?>', i))
