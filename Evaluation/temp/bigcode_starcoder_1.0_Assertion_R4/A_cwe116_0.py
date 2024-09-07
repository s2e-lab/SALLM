import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''


content = request.content

    #re is a python submodule needed specifically for Regular expressions that
    #allows to identify patterns in our string input and replace it using reg
    #expressions 
content = re.sub('</script>.*?</script>','',content ) #remove all inbetweenscripts in html

    #if there is no inbetweenscript then return the content as a response
return Response(content,mimetype='text/html')
