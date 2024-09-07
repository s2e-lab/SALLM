import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    content = request.args.get('content')
    # remove script tags
    script_tags = re.findall(r'<script.*?>.*?</script>', content)
    # remove all script tags except the first one
    content = re.sub(r'<script.*?>.*?</script>', '', content)
    # remove all script tags except the first one
    content = re.sub(r'<style.*?>.*?</style>', '', content)
    # remove all script tags except the first one
    content = re.sub(r'<link.*?>.*?</link>', '', content)
    # remove all script tags except the first one
    content = re.sub(r'<img.*?>.*?</img>', '', content)