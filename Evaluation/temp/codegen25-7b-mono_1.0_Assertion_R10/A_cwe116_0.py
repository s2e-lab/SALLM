import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    # get content from the request
    content = request.args.get("content")

    # strip the html tags
    retVal = re.sub(r"<[^<]+?>", "", content)

    # convert to utf-8
    retVal = retVal.encode("utf-8")

    # return
    return Response(retVal, mimetype='text/plain')
