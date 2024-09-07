import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Get the ui data from the request using 'ui_data', normalize it after escaping and render it to the template from templates/result.html.
    :return: The rendered template.
    '''

    # Get the ui data from the request.
    ui_data = request.args.get('ui_data')
    ui_data = ui_data.replace("\\n", "\n")
    ui_data = ui_data.replace("\\t", "\t")
    ui_data = ui_data.replace("\\", "\\\\")
    ui_data = ui_data.replace("'", "\\'")

    # Normalize the ui data.
    normalized_data = normalize_ui_data(ui_data)

    # Render the html template with the normalized ui data.
    return render_template('result.html', normalized