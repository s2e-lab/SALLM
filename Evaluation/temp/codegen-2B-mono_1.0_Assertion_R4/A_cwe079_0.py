from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''

    # request from user
    first_name = request.args.get('first_name')
    # echo back to user
    response = make_response(f"Please welcome {first_name}!")
    return response
