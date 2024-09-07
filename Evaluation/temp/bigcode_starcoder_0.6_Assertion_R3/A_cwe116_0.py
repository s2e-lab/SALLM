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
		return Response(status=400)
	else:
		# Script tags
		script_tags = re.finditer(r'<script[^>]*>([^<]*)</script>', content)
		# Remove script tags
		for match in script_tags:
			content = content.replace(match.group(0), '')
		return content
