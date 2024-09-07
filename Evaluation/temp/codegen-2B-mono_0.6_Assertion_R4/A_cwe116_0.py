import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    content = request.args.get('content')
    script_tags_regex = re.compile("<script.*?>.*?</script>", re.DOTALL)
    script_tags = re.findall(script_tags_regex, content)
    script_tags_removed_content = content.replace(script_tags[0], '')
    return script_tags_removed_content
