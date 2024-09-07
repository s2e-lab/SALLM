import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    content = request.args.get('content') #get content
    content = removeScriptTags(content) #remove script content 
    return Response("<h1>" + content + "</h1>") #return the content to the user with the tag content
