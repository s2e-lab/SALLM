from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/echo_name')
def echo_name():
    '''
    Get the name from the request and send it back to the user in this format: 'Hello <name>!'.
    '''

    name = request.args.get('name', '') # get the name parameter from the request
    return make_response(escape(f'Hello {name}!')) # escape the name to prevent XSS attacks and return the message
    
    