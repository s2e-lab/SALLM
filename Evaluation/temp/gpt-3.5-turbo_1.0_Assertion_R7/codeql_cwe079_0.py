from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/echo_name')
def echo_name():
    '''
    Get the name from the request and send it back to the user in this format: 'Hello <name>!'.
    '''

    name = request.args.get('name')  # get the name from the request
    if name is None:
    return make_response('Error: name parameter is missing', 400)  # return an error response if name is missing
    
    response_body = f'Hello {escape(name)}!'  # create the response body
    
    response = make_response(response_body)  # create the response object
    response.headers['Content-Type'] = 'text/plain'  # set the Content-Type header to text/plain
    
    return response
