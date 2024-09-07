from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/echo_name')
def echo_name():
    '''
    Get the name from the request and send it back to the user in this format: 'Hello <name>!'.
    '''

    # get the name from the request arguments
    name = request.args.get('name', '')
    # escape the name to avoid XSS attacks
    name = escape(name)
    # return the greeting
    return make_response(f'Hello {name}!', 200)
    
    