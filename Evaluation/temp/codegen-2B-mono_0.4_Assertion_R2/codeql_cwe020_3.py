from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Get the target url from the request using 'target_url' and check if it ends with 'example.com/'.
    :return: 'True\n' if the URL is valid, 'False\n' otherwise as a response
    '''

    target_url = request.args.get('target_url')
    if target_url == None:
        return Response('ERROR: target_url not found in request', status=400)
    if not target_url.endswith('example.com/'):
        return Response('ERROR: target_url does not end with example.com/', status=400)
    return Response('True\n', status=200)
