from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

 #   return jsonify({'result':True,'status_code':200})
    #request is a global variable
    target_url =  request.args.get('target_url', '')
    if (not (target_url == '' or not re.match(r"(www|beta)\.example\.com$", target_url))):
        return (Response("404 Bad Request: target URL does not fit the expected format\n\nUsage: /match_url?target_url=(www|beta).example.com/", status=404, mimetype="text/plain"),404)

    
    # return a 200 status code with a json body
    msg = target_url
    resp = Response(msg, status=200,