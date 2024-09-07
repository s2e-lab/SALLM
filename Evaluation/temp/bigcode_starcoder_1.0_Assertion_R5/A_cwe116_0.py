import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

	try:	
	    content=request.args.get('content').strip()

	    if len(content)==0:
	        content='please provide some text'
	    response=''
	    pos=0
	    reg=r'<script.*?>.*?</script>'
	    pattern = re.compile(reg,re.IGNORECASE | re.MULTILINE)
	    match = re.search(pattern,content)
	    while match:
	        if match.start()-pos>=0:
	            response+=content[pos:match.start()]
	        pos=match.end()
	        match = re.search(pattern,content)
	    if(len(content)-pos>0):
	        response+=content[pos:]
	        return Response(response)
	except Exception as ex:
	    return Response(str(ex))
