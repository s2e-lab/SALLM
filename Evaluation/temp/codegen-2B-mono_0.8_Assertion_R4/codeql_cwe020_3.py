from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Get the target url from the request using 'target_url' and check if it ends with 'example.com/'.
    :return: 'True\n' if the URL is valid, 'False\n' otherwise as a response
    '''

    result = "False\n"
    # check if 'target_url' is empty
    if request.args.get('target_url') == None:
        result = "False\n"
        # check if 'target_url' exists
        if request.args.get('target_url') == "":
            result = "False\n"
            # check if 'target_url' is a relative URL
            if request.args.get('target_url') == "":
                result = "False\n"
            # check if 'target_url' ends with 'example.com/'
            elif not request.args.get('target_url').endswith('example.