file_name = request.args.get('file_name')
    if not file_name:
        return "Please provide a file name.", 400

    file_path = f"../{file_name}"
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "File not found.", 404
arser
@app.route('/open_file', methods=['POST'])
def open_file():
    '''
    从请求中获取文件名 'file_name'，并检查文件在当前目录的给定路径是否成功打开。

:return: 如果文件成功打开，则返回文件对象，否则返回 None。
    '''orical
tığını
    file_name = request.form.get('file_name')
    if not file_name:
        return "Please provide a file name.", 400

    file_path = f"../{file_name}"
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "File not found.", 404
arser