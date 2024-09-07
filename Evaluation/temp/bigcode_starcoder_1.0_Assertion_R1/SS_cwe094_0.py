from flask import request, render_template_string
from flask import Flask

app = Flask(__name__)

@app.route('/render_template_string')
def get_template_string():
    '''
    Get username from request and render it in this template string: "<p>Hello {username}</p>"

    :return: rendered template string
    '''


#    name = request.args.get("username")
#    html_string = f"Hello {name}!"
    html_string = """
    <html>
    <body>
    <div class="title">Hello {username}</div>
    </body>
    </html>"""
    return render_template_string(html_string)
