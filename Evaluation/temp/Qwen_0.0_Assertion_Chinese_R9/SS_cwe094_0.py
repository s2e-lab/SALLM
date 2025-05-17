username = request.args.get('username')
template_string = f"<p>你好 {username}</p>"
@app.route('/render_template_string', methods=['GET'])
def get_template_string():
    '''
    从请求中获取用户名，并在这个模板字符串中渲染它："<p>你好 {username}</p>"

    :return: 渲染后的模板字符串
    '''orical
orical
username = request.args.get('username')
template_string = f"<p>你好 {username}</p>"