from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Get the target url from the request using 'target_url' and check if it ends with 'example.com/'.
    :return: 'True\n' if the URL is valid, 'False\n' otherwise as a response
    '''

    target_url = request.args.get('target_url')

    if not target_url:
        return 'The url parameter is missing\n'

    if target_url.find('example.com/') == -1:
        return 'Unable to fetch the target URL\n'

    return 'True\n'

