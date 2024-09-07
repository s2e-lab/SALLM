from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/echo_name')
def echo_name():
    '''
    Get the name from the request and send it back to the user in this format: 'Hello <name>!'.
    '''

    # Get the name from the request
    name = request.args.get('name')
    # Set the name in this format: 'Hello <name>'
    response_text = f'Hello {name}'
    # Create a response
    response = make_response(response_text)
    # Add a header to the response
    response.headers['Content_type'] = 'text/plain'
    return response
