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
		response = Response(status=400, response="Missing content parameter.")

	# We will assume the response is not JSON until we check
	status = 200
	responseContent = "Success"

	try:
		resultDict = re.sub("<script>(\S|\s)*</script", "", str(content))
		resultDict = json.loads(resultDict)

		# Check to see if the resultDict is a dict or not 
		if isinstance(resultDict, dict):
			status = 200
		else:
			status = 500
			responseContent = "JSON was not formed correctly."
	except:
		status = 500
		responseContent = "Error parsing JSON."		

	response = Response(response=json.