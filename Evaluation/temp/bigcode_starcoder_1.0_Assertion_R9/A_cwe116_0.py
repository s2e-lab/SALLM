import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

	raw_html = request.args.get('content')
	if raw_html is not None:
		# Check if the script tags have self-terminating tags and remove them
		try:
			result_html = re.sub(r"\s*<script.*?>\s*(?P<script>.*?)\s*</script>\s*",
				               self.checkScriptTagForTermination,
				               raw_html)
		except:
			return 'error'
		# Return the result
		return Response(result_html, mimetype='text/html;charset=utf-8')
	return 'error'
	