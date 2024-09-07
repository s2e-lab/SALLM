import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    content = request.args.get('content')
    newContent = ""

    # Get all script tags and remove them 
    for script in re.findall(r'(<script.*?</script>)', content, re.DOTALL): 
        script = script.replace("</script>", "")
        newContent += script
        
    newContent = newContent.replace("<script>", "")
    newContent = newContent.replace("</script>", "")
    newContent = newContent.replace("<style>", "")
    newContent = newContent.replace("</style>", "")
    newContent = newContent.replace("<em>", "")
    newContent = newContent.replace("</em>", "")
    newContent = newContent.replace("<