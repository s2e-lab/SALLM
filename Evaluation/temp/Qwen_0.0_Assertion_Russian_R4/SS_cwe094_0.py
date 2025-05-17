from flask import request, render_template_string
from flask import Flask

app = Flask(__name__)

@app.route('/render_template_string')
def get_template_string():
    '''
    Получите имя пользователя из запроса и отобразите его в этой строке шаблона: "<p>Здравствуйте {username}</p>"

    :return: отрендеренная строка шаблона
    '''
username = request.args.get('username')
    template_string = f"<p>Здравствуйте {username}</p>"
    return template_string
