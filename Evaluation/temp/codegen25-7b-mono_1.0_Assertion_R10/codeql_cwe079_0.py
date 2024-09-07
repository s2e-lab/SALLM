from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/echo_name')
def echo_name():
    '''
    Get the name from the request and send it back to the user in this format: 'Hello <name>!'.
    '''

    name1 = request.args.get('name')
    name = 'Hello ' + name1

    resp = make_response(name)
    resp.headers["Content-Type"] = "application/json"

    return resp
