from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''

    args = request.args
    user_first_name = args['first_name']
    return make_response("Greetings, {user_first_name}".format(user_first_name=user_first_name),"200")
