import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

##    content = request.form['content']
    content = request.args.get('content')
    # Filter out all script tags (keep the contents of script tags).
    filtered_content = re.sub('<script.*?>.*?</script>', '', content)
    # Return the filtered content.
    return Response(filtered_content, mimetype='text/plain')
