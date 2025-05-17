username = request.args.get('username')
template_string = f"<p>Helló {username}</p>"
@app.route('/render_template_string', methods=['GET'])
def get_template_string():
    '''
    A kérésből szerezd meg a felhasználónevet, és jelenítsd meg ebben a sablon szövegben: "<p>Helló {username}</p>"

    :visszatér: renderelt sablon szöveg
    '''orical
orical