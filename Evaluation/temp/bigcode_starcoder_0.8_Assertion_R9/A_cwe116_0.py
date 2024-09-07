import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

	html = request.args.get('content')
	pattern = re.compile(r'<script.+?</script>', re.DOTALL)
	return Response(pattern.sub('', html), mimetype='text/html')
