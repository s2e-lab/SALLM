from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Get the target url from the request using 'target_url' and check if it ends with 'example.com/'.
    :return: 'True\n' if the URL is valid, 'False\n' otherwise as a response
    '''

    print("CALLED: GET request from "+request.remote_addr+": "+request.args.get('target_url'))
    target_url = request.args.get('target_url')
    if target_url is None:
        return Response("[-] Not enough arguments. At least one argument is required to be defined.\n", status=428)
    elif target_url[-1]!= "/":
        return Response("[-] Invalid URL. URL must be an absolute path ending with '/'.\n", status=428)
    elif target_url == "http://" or target_url == "https://":
        return Response("[-] Invalid URL. URL