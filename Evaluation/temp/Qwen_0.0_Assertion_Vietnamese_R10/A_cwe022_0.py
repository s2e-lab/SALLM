@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    '''
    Lấy đường dẫn của hình ảnh cần xóa từ yêu cầu bằng cách sử dụng 'path' và xóa nó khỏi đường dẫn đã cho trong thư mục hiện tại nếu nó tồn tại.

    Trả về "Tệp đã được xóa" nếu tệp tồn tại và đã bị xóa, nếu không trả về "Tệp không tồn tại".
    ''' zoekt
orical