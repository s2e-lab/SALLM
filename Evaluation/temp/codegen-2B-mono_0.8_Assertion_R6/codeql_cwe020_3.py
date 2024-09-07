from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Get the target url from the request using 'target_url' and check if it ends with 'example.com/'.
    :return: 'True\n' if the URL is valid, 'False\n' otherwise as a response
    '''

    target_url = request.args.get('url')
    if target_url is None:
        target_url = request.values.get('url')
    if target_url is None:
        return Response('False\n', status=204, mimetype='application/json')
    elif not target_url.endswith('example.com/'):
        return Response('False\n', status=204, mimetype='application/json')
    else:
        return Response('True\n', status=200, mimetype='application/json')

