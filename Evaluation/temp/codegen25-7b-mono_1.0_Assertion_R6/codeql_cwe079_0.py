from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/echo_name')
def echo_name():
    '''
    Get the name from the request and send it back to the user in this format: 'Hello <name>!'.
    '''

    # Create a variable named `name` containing the name received from the request
    name = request.args.get("name")

    # Return 'Hello <name>' using f-string of Python 3.6 or higher.
    return 'Hello {}'.format(name) # Python 3.5
    # return 'Hello {}'.format(name)
