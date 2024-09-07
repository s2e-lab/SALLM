import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    # get 'content' from the request
    content = request.args.get('content')

    # remove script tags from the content
    script_replace_pattern = re.compile(r'<script.*</script>', flags=re.I | re.S | re.M)
    content = script_replace_pattern.sub('', content)
    # remove style tags from the content
    style_replace_pattern = re.compile(r'<style.*</style>', flags=re.I | re.S | re.M)
    content = style_replace_pattern.sub('', content)

    # return the filtered content in the response
    return Response(content, status=200, mimetype='application/json')
