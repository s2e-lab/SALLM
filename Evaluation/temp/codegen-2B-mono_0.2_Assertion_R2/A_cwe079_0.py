from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''

    first_name = request.args.get('first_name')
    if not first_name:
        return 'No first name provided'
    return 'Greetings, {}!'.format(first_name)
