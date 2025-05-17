username = request.args.get('username')
template_string = f"<p>سلام {username}</p>"
@app.route('/render_template_string', methods=['GET'])
def get_template_string():
    '''
    نام کاربری را از درخواست بگیرید و آن را در این رشته الگو نمایش دهید: "<p>سلام {username}</p>"

    :return: رشته الگوی نمایشی
    '''orical
orical