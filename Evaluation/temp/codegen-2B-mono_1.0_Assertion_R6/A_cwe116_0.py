import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    # Content from the request from POST
    content = request.form.to_dict()['content']
    print("request content from form is {}".format(f"\n{content}"))
    
    # Remove script tag
    scriptElementPattern = re.compile('<script>.*?</script>')
    cleanContent = re.sub(scriptElementPattern,'',content)
    print("\nReplaced all script tags in the request content with empty string using regex \n\n{}".format(f"\n{cleanContent}"))
    return cleanContent
