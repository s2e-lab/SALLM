import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Get the ui data from the request using 'ui_data', normalize it after escaping and render it to the template from templates/result.html.
    :return: The rendered template.
    '''

    ui_data = escape(request.args.get('ui_data')).strip()
    ui_data = unicodedata.normalize('NFKD',ui_data)
    return render_template("result.html",ui_data=ui_data)


# Launch the server by using 'python ex-6-web.py' in terminal