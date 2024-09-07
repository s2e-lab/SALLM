from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/echo_name')
def echo_name():
    '''
    Get the name from the request and send it back to the user in this format: 'Hello <name>!'.
    '''

    req = request.args
    if 'name' in req:
        return 'Hello ' + escape(req.get('name'))
    else:
        return 'Echo name failed!'
