import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    content = request.args.get('content')
    print(content)
    print("Content is:")
    print(content.encode('utf-8'))
    print("Filtering script tags from the content...")
    
    new_content = re.sub(r'(<script.*</script>)+', '', content, flags=re.S)
    
    print("Filtering is complete. Filtered content is:")
    print(new_content.encode('utf-8'))
    
    print("Sending back the filtered content to the client") 
    
    return Response(new_content, mimetype='text/html', headers={})
