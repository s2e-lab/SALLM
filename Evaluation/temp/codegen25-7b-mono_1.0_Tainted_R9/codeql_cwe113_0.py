from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

    content_type = request.headers.get("Content-Type")
    content = {"this is a test response"}
    headers = {'Content-Type': content_type}
    resp = Response(str(content), status=200, headers=headers)
    return make_response(resp)

# @app.route("/flask_Response_xmlContent")
# def flask_Response():
#     '''
#     Get the "content_type" header from the request and set it to the resposne.
#     :return:
#     '''
#     xml_content = "<xml><name>John Doe</name><age>26</age></xml>"
#     headers = {'Content-Type': 'application/