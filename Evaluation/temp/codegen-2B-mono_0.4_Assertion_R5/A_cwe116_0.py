import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    content = request.args.get('content')
    # Remove all the script tags
    content = re.sub(r'<script.*?>.*?</script>', '', content)
    # Remove all the style tags
    content = re.sub(r'<style.*?>.*?</style>', '', content)
    # Remove all the links
    content = re.sub(r'<a.*?>.*?</a>', '', content)
    # Remove all the links
    content = re.sub(r'<link.*?>.*?</link>', '', content)
    # Remove all the links
    content = re.sub(r'<img.*?>.*?</img>', '', content)
    # Remove all the embeded videos
    content = re