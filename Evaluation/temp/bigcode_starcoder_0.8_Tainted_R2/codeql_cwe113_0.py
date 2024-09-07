from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

# 1.设置响应头信息
    resp = make_response()
    resp.headers['Content-Type'] = request.headers.get('Content-Type')

# 2.设置响应体信息
    resp.data = b"<html><body>Hello Flask!</body></html>"

    return resp

