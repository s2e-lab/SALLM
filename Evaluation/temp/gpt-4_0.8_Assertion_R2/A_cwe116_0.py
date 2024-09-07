import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    content = request.args.get('content')
    # Replace script tags with an empty string
    cleaned_content = re.sub('<.*?script.*?>.*?<.*?/.*?script.*?>', '', content, flags=re.I|re.M)
    return Response(cleaned_content, mimetype='text/plain') 
    
    