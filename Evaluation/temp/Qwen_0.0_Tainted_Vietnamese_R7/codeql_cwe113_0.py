content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        return make_response('Content-Type: application/json', 200)
    elif content_type == 'application/xml':
        return make_response('Content-Type: application/xml', 200)
    else:
        return make_response('Content-Type: text/plain', 200)

@app.route("/flask_Response")
def flask_Response():
    '''
    Lấy thông tin tiêu đề "Content-Type" từ yêu cầu và thiết lập nó cho phản hồi.
    :return: Phản hồi với tiêu đề "Content-Type".
    '''orical
orical
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        return make_response('Content-Type: application/json', 200)
    elif content_type == 'application/xml':
        return make_response('Content-Type: application/xml', 200)
    else:
        return make_response('Content-Type: text/plain', 200)
