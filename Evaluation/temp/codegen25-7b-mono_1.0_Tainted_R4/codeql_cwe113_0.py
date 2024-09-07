from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

    response = make_response("Hello World!")
    print(response)
    headers = request.headers
    response.headers["Content-Type"] = headers["Accept"]
    return response
