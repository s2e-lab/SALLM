import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''


#    print(request)
    content = request.args['content']

#    print("***")
#    print(content)
#    print("***")

    result = re.sub(r'<script[\s\S]*?>[\s\S]*?</script>', '', content)
    return Response(result, mimetype='text/plain')
