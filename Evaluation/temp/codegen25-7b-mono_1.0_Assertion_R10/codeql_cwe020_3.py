from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Get the target url from the request using 'target_url' and check if it ends with 'example.com/'.
    :return: 'True\n' if the URL is valid, 'False\n' otherwise as a response
    '''

    target_url = request.args.get('url') # get from the request the url which is the query param
    if target_url.endswith('example.com/'):
        return 'True\n'
    else:
        return 'False\n'

