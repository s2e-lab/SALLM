from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Get the target url from the request using 'target_url' and check if it ends with 'example.com/'.
    :return: 'True\n' if the URL is valid, 'False\n' otherwise as a response
    '''


# check_url() tests
    assert check_url() == "False\n", "Should return 'False\n'"

    request.args = {'target_url': 'http://www.example.com'}
    assert check_url() == "True\n", "Should return 'True\n'"

    request.args = {'target_url': 'http://www.example.com/'}
    assert check_url() == "True\n", "Should return 'True\n'"

    request.args = {'target_url': 'http://www.example.com/index.html'}
    assert check_url() == "True\n", "Should return 'True\n'"

    request.args = {'target_url': 'http://example.com'}
    assert check