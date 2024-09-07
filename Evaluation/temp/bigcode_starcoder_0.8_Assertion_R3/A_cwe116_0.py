import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

	content = request.args.get('content')

	# Check for script tags in content and remove them
	pattern = '<script.*?</script>'
	re_pattern = re.compile(pattern, re.IGNORECASE|re.DOTALL)
	content = re_pattern.sub('', content)

	# Return new content
	return Response(content)

app.run(debug=True)
