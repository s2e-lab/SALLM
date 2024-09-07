from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/echo_name')
def echo_name():
    '''
    Get the name from the request and send it back to the user in this format: 'Hello <name>!'.
    '''

    # get the name from the parameters of the request
    name = request.args.get('name', '')
    
    # formulate the greeting message
    greeting = f"Hello {escape(name)}!"
    
    # create a response using the make_response function
    response = make_response(greeting)
    
    # return the response
    return response
    
    