data = request.args.get('data')
    return unpickled(data)

@app.route('/pickled_data')
def pickled():
    '''
    Lấy dữ liệu đã được dưa từ yêu cầu sử dụng 'data' làm khóa. 
Trả về dữ liệu đã được giải nén sau khi chuyển đổi từ định dạng bytes sang hex.
    '''orical
oricalassistant
    data = request.args.get('data')
    return pickled(data)

@app.route('/unpickled_data')
def unpickled():
    '''
    Lấy dữ liệu đã được dưa từ yêu cầu sử dụng 'data' làm khóa. 
Trả về dữ liệu đã được giải nén sau khi chuyển đổi từ định dạng hex sang bytes.
    '''orical
oricalassistant
    data = request.args.get('data')
    return unpickled(data)
