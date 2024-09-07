from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

# <start id="doc-content-type"/>
    resp = make_response("<h1>" + request.headers['Content-Type'] + "</h1>")
    resp.headers['Content-Type'] = request.headers['Content-Type']
# <end id="doc-content-type"/>
    return resp
