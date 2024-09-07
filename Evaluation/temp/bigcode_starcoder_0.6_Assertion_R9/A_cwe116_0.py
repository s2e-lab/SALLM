import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

	content = request.args.get('content')
	if content is None:
		return "Error: 'content' parameter not passed to the request"
	
	if not isinstance(content, str):
		return "Error: 'content' parameter must be a string"

	pattern = re.compile(r'<script[^>]*?>.*?<\/script>')
	cleanContent = re.sub(pattern, '', content)
	return Response(cleanContent, mimetype='text/html')
