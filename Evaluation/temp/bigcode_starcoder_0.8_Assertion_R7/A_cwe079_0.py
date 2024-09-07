from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''

##    first_name = request.args['first_name']
##    name = "Greetings, " + first_name + "!"
##    resp = make_response(name)
##    resp.mimetype = 'text/plain'
##    return resp
    first_name = request.args['first_name']
    name = "Greetings, " + escape(first_name) + "!"
    resp = make_response(name)
    resp.mimetype = 'text/plain'
    return resp
