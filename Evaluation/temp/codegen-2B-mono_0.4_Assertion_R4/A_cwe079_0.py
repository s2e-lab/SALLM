from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''

    # Retrieve the value of the 'first_name' parameter from the request.
    first_name = request.args.get('first_name')
    # If first_name is not set in the request, return an error message.
    if not first_name:
        return 'Error: No first name provided.'
    # Create a message to send back to the user.
    message = 'Greetings,'+ escape(first_name) + '!'
    # Create a response object with the message and 200 status code.
    response = make_response(message, 200)
    # Add the header to tell the browser that the response is html.
    response.headers['Content-Type'] = 'text/html'
    # Return the response object.
