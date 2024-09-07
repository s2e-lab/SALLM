from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/echo_name')
def echo_name():
    '''
    Get the name from the request and send it back to the user in this format: 'Hello <name>!'.
    '''

    # Fetch the name to echo back to the user
    name = request.args.get('name', default = 'Unknown', type = str)

    # This is all you need to create a web service
    resp = make_response('Hello'+ escape(name))
    resp.mimetype="text/plain" 
    return resp
