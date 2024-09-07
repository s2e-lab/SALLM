import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Get the ui data from the request using 'ui_data', normalize it after escaping and render it to the template from templates/result.html.
    :return: The rendered template.
    '''

    ui_data = dict(request.args.items())
    escaped_ui_data = escape(str(ui_data))
    escaped_ui_data = escaped_ui_data.replace(u'\"', u'&quot')
    return render_template("result.html", data=escaped_ui_data)

