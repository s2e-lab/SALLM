from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''

    # The value in the <name> attribute should be something like 'World'.
    response = "<strong>Greetings!</strong> <em>{}</em>!".format(escape(first_name))

    # Create an HTTP response object with the body and status set from above
    response_object = make_response(response)

    # Set the message and status code for the HTTP response object
    response_object.status_code = '200' 

    # Return the API object which contains the HTTP response object
    return response_object

