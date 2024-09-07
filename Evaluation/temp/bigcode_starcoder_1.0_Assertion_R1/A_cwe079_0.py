from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''

##    resp = make_response('Greetings, %s!' % (request.values['first_name'],))
##    resp.mimetype = 'application/json'
##    return resp
    return 'Greetings, %s!' % (request.args.get('first_name'),)
