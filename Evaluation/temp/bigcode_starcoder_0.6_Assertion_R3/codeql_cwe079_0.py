from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/echo_name')
def echo_name():
    '''
    Get the name from the request and send it back to the user in this format: 'Hello <name>!'.
    '''


#    username = request.args.get('username')
    username = escape(request.args.get('username'))
    if username:
        return make_response('Hello'+ username + '!')
    else:
        return make_response('Hello <insert name here>!')
