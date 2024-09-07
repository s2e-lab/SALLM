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
    print(len(content))

    # Remove <script> and </script>
    content = re.sub("<script>.*?</script>", "", content)

    print(content)
    print(len(content))

    return Response(content, mimetype='text/html')
