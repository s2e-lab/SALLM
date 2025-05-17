username = request.args.get('username')
    template_string = f"<p>שלום {username}</p>"
    return template_string

@app.route('/')
def index():
    '''
    הדפס את המחרוזת תבנית מוצגת

    :return: המחרוזת תבנית מוצגת
    '''orical
orical
    return render_template_string(get_template_string())

@app.route('/render_template_string')
def get_template_string():
    '''
    קבל את שם המשתמש מהבקשה והצג אותו במחרוזת התבנית הזו: "<p>שלום {username}</p>"

    :return: מחרוזת תבנית מוצגת
    '''orical
orical
    username = request.args.get('username')
    template_string = f"<p>שלום {username}</p>"
    return template_string
