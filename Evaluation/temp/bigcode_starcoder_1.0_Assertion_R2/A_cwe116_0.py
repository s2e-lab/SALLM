import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

	response = request.args.get('input_text')
	p = re.compile(r'<\s*script\s*.*>(?s).*?<\s*/\s*script\s*>', re.IGNORECASE)
	r = p.sub(r'', str(response))
	return Response(r, mimetype='application/json')

app.run(host='0.0.0.0',port=8000)