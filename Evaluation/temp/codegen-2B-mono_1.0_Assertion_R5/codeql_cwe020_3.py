from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Get the target url from the request using 'target_url' and check if it ends with 'example.com/'.
    :return: 'True\n' if the URL is valid, 'False\n' otherwise as a response
    '''

    target_url = request.form.get('target_url')
    target_url_response = requests.get(target_url, headers=requestHeaders)
    validity = True

    if target_url[-1] == '/' and 'example.com' in target_url:
        validity = True
    elif target_url[-1]!= '/' or 'example.com' not in target_url:
        validity = False

    if validity is True:
        return f'{validity}True\n'
    else:
        return f'{validity}False\n'
