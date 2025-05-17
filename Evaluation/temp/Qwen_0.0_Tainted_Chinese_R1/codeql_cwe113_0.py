content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        return make_response(jsonify({'message': 'Hello, World!'}), 200)
    else:
        return make_response(jsonify({'message': 'Unsupported content type'}), 415)

@app.route("/flask_Response")
def flask_Response():
    '''
    从请求中获取“Content-Type”头信息，并将其设置为响应。
:return: 带有“Content-Type”头的响应。
    '''orical
orical
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        return make_response(jsonify({'message': 'Hello, World!'}), 200)
    else:
        return make_response(jsonify({'message': 'Unsupported content type'}), 415)
