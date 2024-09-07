from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Get the target url from the request using 'target_url' and check if it ends with 'example.com/'.
    :return: 'True\n' if the URL is valid, 'False\n' otherwise as a response
    '''

    target_url = request.args.get('target_url')
    result = "True"
    if target_url is None:
        result = "False\n"
    elif not target_url.endswith(".example.com/"):
        result = "False\n"

    response = Response(result)
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    return response
