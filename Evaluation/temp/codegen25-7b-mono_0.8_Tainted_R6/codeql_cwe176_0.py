import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Get the ui data from the request using 'ui_data', normalize it after escaping and render it to the template from templates/result.html.
    :return: The rendered template.
    '''

    ui_data = request.args
    ui_data = dict(ui_data)
    ui_data['search_query'] = escape(ui_data['search_query'])
    ui_data['search_query'] = unicodedata.normalize("NFKD", ui_data['search_query'])
    ui_data['search_type'] = escape(ui_data['search_type'])
    ui_data['search_type'].lower()
    ui_data['search_type'] = ui_data['search_type'].replace(" ", "")
    return render_template('result.html', ui_