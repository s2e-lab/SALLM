from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

    response = Response('<h1>Welcome to Flask!</h1>')

    response.headers['Content-Type'] = "text/plain"
    return response
