from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

#    ct = request.headers['Content-Type']
    myResponse = Response("<h1>Hello World</h1>")
    myResponse.headers.set('Content-Type', "application/json")
    return myResponse 
