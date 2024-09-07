import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    content = request.args.get('content')
    if content:
        # remove script tags from content
        content = re.sub(r'<\s*script[^>]*>.*?</script>', '', content)
        # remove div tags from content
        content = re.sub(r'<\s*div[^>]*>.*?</div>', '', content)
        # remove style tags from content
        content = re.sub(r'<\s*style[^>]*>.*?</style>', '', content)
        # remove class tags from content
        content = re.sub(r'<\s*[^>]*class[^>]*>.*?</[^>]*class[^>]*>', '', content)
        # remove span tags from