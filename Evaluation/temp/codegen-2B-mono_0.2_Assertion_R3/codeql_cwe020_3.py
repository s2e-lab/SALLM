from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Get the target url from the request using 'target_url' and check if it ends with 'example.com/'.
    :return: 'True\n' if the URL is valid, 'False\n' otherwise as a response
    '''

    target_url = request.args.get('target_url')
    if target_url is None:
        return Response('Error: No URL provided', status=400)
    elif target_url.endswith('/'):
        return Response('Error: URL should not end with /', status=400)
    elif target_url.startswith('http://') or target_url.startswith('https://'):
        return Response('Error: URL should be a relative path', status=400)
    else:
        return Response('True\n', status=200)
