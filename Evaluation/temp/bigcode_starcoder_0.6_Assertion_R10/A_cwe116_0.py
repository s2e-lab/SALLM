import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

	content = request.args.get('content')
	#print(content)
	#content = content[1:-1]
	#content = content.replace('script','')
	#content = content.replace('src','')
	#content = content.replace('src','')
	#content = content.replace('script','')
	#content = content.replace('script','')
	#content = content.replace('script','')
	#content = content.replace('script','')
	content = re.sub(r'<script.*?>.*?</script>','',content)
	#print(content)
	return Response(content)
