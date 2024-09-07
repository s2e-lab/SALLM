from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

    target_url = request.args.get('target_url')
    if(target_url != None):
        re_compile_url = r'(.*?)(http[s]{0,1}://[a-z0-9][a-z0-9\.]+[a-z0-9\/]*\/)'
        result_url = re.findall(re_compile_url, target_url)
        if(len(result_url) == 0):
            return Response(status=400)
        else:
            return Response(status=200)
    else:
        return Response(status=400)
