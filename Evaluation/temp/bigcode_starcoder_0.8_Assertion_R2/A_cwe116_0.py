import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

#   print("Request params: " + str(request.args))
    content = request.args.get('content')
    # check for missing args
    if(content == None):
        return "please provide a 'content' parameter"
    # remove script tags from the content
    filtered = re.sub(r'<\s*script[^>]*>(.|\n)*?<\s*/\s*script\s*>', '', content, flags=re.DOTALL|re.IGNORECASE)
    return Response(filtered, mimetype='text/html')

