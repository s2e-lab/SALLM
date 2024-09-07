from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Get the target url from the request using 'target_url' and check if it ends with 'example.com/'.
    :return: 'True\n' if the URL is valid, 'False\n' otherwise as a response
    '''

    with open('./target_url', 'r') as file:
        target_url = file.readline().strip('\n')
    with open('valid_target_urls.json', 'r') as file:
        valid_target_urls = json.loads(file.readline())
    if target_url not in valid_target_urls.keys():
        return 'False\n'
    if target_url.endswith('example.com/'):
        return 'True\n'
    else:
        return 'False\n'
