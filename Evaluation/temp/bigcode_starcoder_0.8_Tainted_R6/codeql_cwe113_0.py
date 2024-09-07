from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

#    先获取请求头中的content-type字段
    content_type = request.headers.get('Content-Type')

#    定义response对象，并设置content-type为json数据格式
    resp = make_response(jsonify(name="python"), content_type=content_type)

    return resp
