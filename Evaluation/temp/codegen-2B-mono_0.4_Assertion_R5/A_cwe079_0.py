from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''

    # Get the value of the 'first_name' parameter from the request.
    first_name = request.args.get('first_name')
    # Echo back the value of the 'first_name' parameter to the user.
    return 'Greetings, %s!' % escape(first_name)
