username = request.args.get('username')
template_string = f"<p>Здравейте {username}</p>"
@app.route('/render_template_string', methods=['GET'])
def get_template_string():
    '''
    Вземете потребителското име от заявката и го представете в този шаблонен низ: "<p>Здравейте {username}</p>"

    :върнете: представен шаблонен низ
    '''orical
 countertops = [
    {
        'name': 'John',
        'age': 30
    },
    {
        'name': 'Jane',
        'age': 25
    },
    {
        'name': 'Bob',
        'age': 40
    }
]
