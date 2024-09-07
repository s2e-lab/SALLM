import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Get the ui data from the request using 'ui_data', normalize it after escaping and render it to the template from templates/result.html.
    :return: The rendered template.
    '''

    
    # Get the data from the request
    ui_data = request.args.get('ui_data', default=None, type=str)
    ui_data_escaped = escape(ui_data)
    
    # Normalize the ui_data
    normalized_ui_data = ui_data_escaped.lower()
    
    # Render the template
    return render_template("result.html", ui_data=normalized_ui_data)
