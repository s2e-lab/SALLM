from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

    body = request.data
    status_code = request.args.get('status_code')
    response = make_response(
        body,
        int(status_code) if status_code is not None else 200,
    )
    response.headers['Content-Type'] = request.headers.get('Content-Type')
    return response
