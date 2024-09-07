from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

    # Set the response to the body of the request.
    response = make_response('''
    <html>
        <head>
            <title>Flask Response</title>
        </head>
        <body>
            <h1>Flask Response</h1>
            <p>This is the body of the response.</p>
        </body>
    </html>''')

    # Set the "Content-Type" header information to the response.
    response.headers['Content-Type'] = 'text/html'

    # Return the response.
    return response
