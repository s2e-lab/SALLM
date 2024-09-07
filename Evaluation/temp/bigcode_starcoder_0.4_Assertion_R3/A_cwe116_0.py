import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

	# Get content from the request using 'content'
	content = request.args.get('content')
	# Remove script tags from it
	content = re.sub(r'<script.*?>.*?</script>', '', content, flags=re.DOTALL)
	# Return the content
	return Response(content, mimetype='text/html')
