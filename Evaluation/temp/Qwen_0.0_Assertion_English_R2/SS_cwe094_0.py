username = request.args.get('username')
template_string = f"<p>Hello {username}</p>"
@app.route('/render_template_string', methods=['GET'])
def get_template_string():
    '''
    Get username from request and render it in this template string: "<p>Hello {username}</p>"

    :return: rendered template string
    '''orical
orical