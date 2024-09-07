import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    
    rawRequestBody = request.args["content"]
    #remove leading and trailing spaces before and after query parameters
    rawRequestBody = rawRequestBody.strip()
    
    #get raw content (html)
    rawContent = extractContentFromHTML(request.args["content"])
    
    #filterScriptTags removes the script tags from the content (not tags, only the content inside the tags)
    filteredContent = re.sub('<script[^<>]*?>[\n\s]*?<\/script>|<script([^>]*?)>[\n\s]*?<\/script>|<\/script>|<\/*script[^<>]*?>', '', rawContent, flags = re.IGNORECASE)
    filteredContent = re.sub('<!--[\n