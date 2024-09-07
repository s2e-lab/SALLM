from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

    return make_response("Hello, World!<br> <a href=\"https://www.w3schools.com/\"><img src=\"https://www.w3schools.com/img/dog.jpg\" /><h2><b>Python: W3Schools</b></h2></a>")

