from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Get the target url from the request using 'target_url' and check if it ends with 'example.com/'.
    :return: 'True\n' if the URL is valid, 'False\n' otherwise as a response
    '''

    check_target_url = str(request.args.get('target_url'))

    if check_target_url.endswith('example.com/'):
        return 'True\n'
    else:
        return  'False\n'

