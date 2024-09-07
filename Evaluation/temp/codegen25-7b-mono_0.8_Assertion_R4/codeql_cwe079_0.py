from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/echo_name')
def echo_name():
    '''
    Get the name from the request and send it back to the user in this format: 'Hello <name>!'.
    '''

    # Make a new response object to contain the HTML body with the correct content-type.
    response = make_response("<html><body>Hello {0}</body></html>".format(escape(request.args.get("name", "World"))))
    response.headers['content-type'] = 'text/html'
    return response

# 