import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

#    response = Response('<script>alert("You are a hacker.");</script>')
#    print "request.headers: " + str(request.headers) + " request.args: " + str(request.args) + " request.cookies: " + str(request.cookies)
    requestContent = request.args.get('content')
    print  "request.arg Content: %s " % requestContent
#    response.headers['X-XSS-Protection'] = "0"
     
    if requestContent is not None:
		print "Removing script tags"	
		return re.sub(r'<script[^>]*?>\s*?</script>|<script type.*?>.*?</script>|<script>', "", requestContent)
    
    return "Failed"
#     response.headers['Accept'] = "application/json"
#     response.headers['Content-Type'] = "application/json"
