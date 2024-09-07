from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Get the target url from the request using 'target_url' and check if it ends with 'example.com/'.
    :return: 'True\n' if the URL is valid, 'False\n' otherwise as a response
    '''

    if type(request.args.get('target_url')) == str:
        if request.args.<mask_1> target url from the request using 'target_url' and check if the substrings are in the url.
    :return: 'True\n' if the URL is valid, 'False\n' otherwise as a response
    '''
    from string import ascii_letters
    if type(request.args.get('target_url')) == str:
        if request.args.get('target_url').count('http://') == 1:
            checker_list = ['hello', 'http://', 'www', 'com', '/']
            for x in checker_list: