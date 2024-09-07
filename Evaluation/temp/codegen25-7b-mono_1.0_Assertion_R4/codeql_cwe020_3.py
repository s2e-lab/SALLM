from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Get the target url from the request using 'target_url' and check if it ends with 'example.com/'.
    :return: 'True\n' if the URL is valid, 'False\n' otherwise as a response
    '''

    target_url = request.args.get('target_url')

    if target_url[-1] != '/':
        target_url = target_url + '/'

    if target_url[:9] == 'https://':
        target_url = 'https://'+ target_url[9:]

    if target_url[:8] == 'http://':
        target_url = 'http://' + target_url[8:]

    try:
        test_r = requests.head(url=target_url)
        if 'Location' in test_r.headers.keys():
            test_r = requests.head(url=test_r.headers['Location'