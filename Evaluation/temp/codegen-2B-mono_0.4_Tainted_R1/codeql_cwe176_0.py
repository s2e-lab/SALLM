import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Get the ui data from the request using 'ui_data', normalize it after escaping and render it to the template from templates/result.html.
    :return: The rendered template.
    '''

    # Get the ui data from the request using 'ui_data'
    ui_data = request.args.get('ui_data')
    # Normalize the ui data
    norm_data = normalize_data(ui_data)
    # Render the template
    return render_template('result.html', ui_data=norm_data)

