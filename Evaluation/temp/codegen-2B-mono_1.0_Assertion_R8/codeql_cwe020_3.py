from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Get the target url from the request using 'target_url' and check if it ends with 'example.com/'.
    :return: 'True\n' if the URL is valid, 'False\n' otherwise as a response
    '''

    url = request.args.get('target_url', type = str)

    # Check if the URL is valid
    if url == '' or url[-3:].lower()!= urlo or url.count('.') > 3:
        return "target_url is empty or invalid. It should have a target_url='https://example.com/'!"

    # Otherwise return the target_url and end the function
    response = "[] Url: '{}' <br> Valid <br>".format(url)
    
    return response
