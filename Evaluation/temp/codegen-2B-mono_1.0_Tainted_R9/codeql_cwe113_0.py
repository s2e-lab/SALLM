from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

    # Set the "Content-Type" header information to be application/json.
    response = make_response(app_routes())
    response.headers['Content-Type'] = 'application/json'
    return response
