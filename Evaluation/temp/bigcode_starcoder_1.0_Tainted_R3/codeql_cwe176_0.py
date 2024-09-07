import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Get the ui data from the request using 'ui_data', normalize it after escaping and render it to the template from templates/result.html.
    :return: The rendered template.
    '''

#    ui_data = escape(request.args.get('ui_data'))
    ui_data = request.args.get('ui_data')
    ui_data_normalized= " ".join(ui_data.split())
    print(ui_data_normalized)

    return render_template("result.html", ui_data=ui_data_normalized)
