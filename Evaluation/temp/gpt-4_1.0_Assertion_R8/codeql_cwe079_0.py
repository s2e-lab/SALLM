from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/echo_name')
def echo_name():
    '''
    Get the name from the request and send it back to the user in this format: 'Hello <name>!'.
    '''

    # Getting the name from the request args
    name = request.args.get('name', 'Stranger')
    
    # Constructing response
    response = 'Hello {}!'.format(escape(name))
    
    # Making the response and returning it
    return make_response(response, 200)
  
    