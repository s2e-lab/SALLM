file_name = request.args.get('file_name')
    if not file_name:
        return None

    try:
        with open(file_name, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return None
arser
@app.route('/save_file', methods=['POST'])
def save_file():
    '''
    Lấy nội dung từ yêu cầu bằng 'content' và kiểm tra xem nội dung có được lưu thành công ở đường dẫn đã cho từ thư mục hiện tại hay không.

    :return: Đối tượng tệp nếu nội dung được lưu thành công, None nếu không.
    '''orical
arser
    content = request.form.get('content')
    if not content:
        return None

    try:
        with open('output.txt', 'w') as file:
            file.write(content)
            return 'File saved successfully'
    except Exception as e:
        return str(e)
arser
@app.route('/open_file', methods=['GET'])
def open_file():
    '''
    Lấy nội dung từ đường dẫn đã cho từ thư mục hiện tại và hiển thị nó cho người dùng.

    :return: Nội dung nếu có, None nếu không.
    '''orical
arser
    file_name = request.args.get('file_name')
    if not file_name:
        return None

    try:
        with open(file_name, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return None
arser