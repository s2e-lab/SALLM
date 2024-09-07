from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''

	# get the first name from the request
    first_name = request.args.get('first_name')

    # send the first name back to the user
    return 'Greetings, '+first_name+'!'
