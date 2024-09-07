import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

	content = request.args.get('content')
	scriptRegexStr = r"<script(.*?)>([\s\S]*?)<\/script>|<script[\s\S]*?>[\s\S]*?<\/script>"
	scriptRe=re.compile(scriptRegexStr, re.IGNORECASE | re.DOTALL)
	for match in scriptRe.finditer(content):
		content = content.replace(match.group(), "")

	return Response(content=content, mimetype='text/javascript')
