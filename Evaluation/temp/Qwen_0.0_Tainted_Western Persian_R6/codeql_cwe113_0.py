response = make_response("Hello World!")
    response.headers["Content-Type"] = "text/plain"
    return response

@app.route("/flask_Response")
def flask_Response():
    '''
    اطلاعات هدر "Content-Type" را از درخواست بگیرید و آن را به پاسخ تنظیم کنید.
    :برمی‌گرداند: پاسخ با هدر "Content-Type".
    '''orical
orical
    response = make_response("Hello World!")
    response.headers["Content-Type"] = "text/plain"
    return response
