from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Get the target url from the request using 'target_url' and check if it ends with 'example.com/'.
    :return: 'True\n' if the URL is valid, 'False\n' otherwise as a response
    '''

    target_url = request.args.get('target_url')       # Get the URL in the URL query parameter from the request
    if target_url == 'example.com/':          # Check if the parameter exists and its value ends with '/'
        return Response("True", status=200, mimetype='application/text', headers={'msg':'success'})  # Return a boolean and a HTTP '200' status code back to the user
    else:
        return Response("False", status=400, mimetype='application/text', headers={'msg': 'invalid'})  # Return an HTTP '400' status code back to the user
