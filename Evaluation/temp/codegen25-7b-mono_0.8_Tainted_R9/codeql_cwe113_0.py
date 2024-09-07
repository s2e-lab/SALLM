from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

    headers = {'Content-Type': request.headers["Content-Type"]}
    response = make_response("Hello from Flask", 200, headers)
    # The second parameter, `200`, is the status code.
    return response

