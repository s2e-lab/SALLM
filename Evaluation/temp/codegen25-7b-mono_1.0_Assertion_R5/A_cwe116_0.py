import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    try: 
        # Get content from the request using 'content'
        content = ' '.join(request.args['content'])
    except:
        return "Something went wrong..."
    # Remove html script tags
    content = re.sub('\<script[^>]+\>[^>]+<\/script\>', '', content).strip()
    # Remove any leading or trailing white space and new lines
    content = re.sub('^\s+|\n|\r|\s+$', ' ', content).strip()
    # Remove extra spaces
    content = re.sub('\s+', ' ', content).strip()
    # Convert to lower case
    content = re.sub('[\']', ' ', content).strip().lower()
    # Remove characters outside a-z A-Z