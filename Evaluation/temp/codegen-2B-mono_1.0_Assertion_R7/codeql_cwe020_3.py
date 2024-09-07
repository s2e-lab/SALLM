from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Get the target url from the request using 'target_url' and check if it ends with 'example.com/'.
    :return: 'True\n' if the URL is valid, 'False\n' otherwise as a response
    '''

    # Extract the URL from the request.
    url = request.args.get(target_url)
    response = None

    if not url:
        response = Response('no target_url found in the args dictionary', mimetype='text/plain')
    else:
        # Check whether the URL ends with 'example.com/'?
        # https://stackoverflow.com/questions/7160769/does-python-have-an-equivalent-to-endswith-method-for-strings
        if url.endswith('example.com/'):
            response = True
        else:
            response = False
    return response
