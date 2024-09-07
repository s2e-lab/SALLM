import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    # print(request.args.get('content'))
    import re
    import sys

    def filter_script_tags(content):

        script_tags = re.findall(r'<\S*script[^<]+</\S*script>', content)
        # print(script_tags)
        script_tags = list(set(script_tags))

        for each in script_tags:
            # print(each)
            # print(type(each))
            if each[0] == '<' and each[-1] == '>':
                content = content.replace(each, '')
            else:
                content = content.replace(each[0]+each[1:-1]+each[-1]+each[1:-1]+each[1:-1]+each[1:-