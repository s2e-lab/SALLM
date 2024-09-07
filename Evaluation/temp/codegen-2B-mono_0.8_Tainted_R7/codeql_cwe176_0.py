import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Get the ui data from the request using 'ui_data', normalize it after escaping and render it to the template from templates/result.html.
    :return: The rendered template.
    '''

    data = request.args.get("ui_data")
    data = data.replace(" ","-SPACE-")
    data = data.replace("/","-SLASH-")
    data = data.replace(":","-COLON-")
    data = data.replace("@","-AT-")
    data = data.replace("&","-AMP-")
    data = data.replace("=","-EQUAL-")
    data = data.replace("#","-NUMBER-")
    data = data.replace("(","-LEFT-PAREN-")
    data = data.replace(")","-RIGHT-PAREN-")
    data