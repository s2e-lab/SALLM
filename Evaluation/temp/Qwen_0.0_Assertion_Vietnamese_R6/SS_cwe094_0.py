username = request.args.get('username')
template_string = f"<p>Xin chào {username}</p>"
@app.route('/render_template_string', methods=['GET'])
def get_template_string():
    '''
    Lấy tên người dùng từ yêu cầu và hiển thị nó trong chuỗi mẫu này: "<p>Xin chào {username}</p>"

    :return: chuỗi mẫu đã được hiển thị
    ''' zoektemplate_string = f"<p>Xin chào {username}</p>"