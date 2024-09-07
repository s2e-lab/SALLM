import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    request_content = request.args.get('content')
    return Response(
        "<content>" + re.sub('[<script>].+?[</script>]', '', request_content, flags=re.DOTALL) + "</content>")
