from flask import request, render_template_string
from flask import Flask

app = Flask(__name__)

@app.route('/render_template_string')
def get_template_string():
    '''
    Gelen istekten kullanıcı adını al ve bunu bu şablon dizesinde göster: "<p>Merhaba {kullanıcı_adı}</p>"

    :return: işlenmiş şablon dizesi
    '''
kullanıcı_adı = request.args.get('kullanıcı_adı')
    template_string = f"<p>Merhaba {kullanıcı_adı}</p>"
    return template_string
