import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    content = request.args.get('content')
    # remove html tags
    content = re.sub(r'<script.*?</script>', '', content, flags=re.DOTALL)
    # remove html comments
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
    # remove html tags
    content = re.sub(r'<.*?>', '', content, flags=re.DOTALL)
    # remove html comments
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
    # remove html tags
    content = re.sub(r'<.*?>', '', content, flags=re.DOTALL)
    # remove html comments