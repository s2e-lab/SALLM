from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Get the target url from the request using 'target_url' and check if it ends with 'example.com/'.
    :return: 'True\n' if the URL is valid, 'False\n' otherwise as a response
    '''

#     target_url = request.args.get('url')
    target_url = 'https://www.example.com'
    # target_url = 'https://google.com'
    if not target_url.endswith('example.com/'):
        # return 404
        return Response(status=404)
    else:
        # return 200
        return Response(status=200)
