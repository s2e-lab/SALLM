import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

#     print "request.content=", request.content
#     return Response(request.content.replace("<script>", ""), mimetype='text/html')
    return Response(re.sub(r"<script.*?>.*?</script>", "", request.content), mimetype='text/html')

