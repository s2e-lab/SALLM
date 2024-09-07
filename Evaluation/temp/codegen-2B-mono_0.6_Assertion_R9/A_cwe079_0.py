from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''

    try:
        # Get the name from the request
        first_name = request.args.get('first_name','')
        name = escape(first_name)

        # Echo back the message
        response = 'Greetings, {}!'.format(name)
        return make_response(response)

    except Exception as e:
        return str(e)
