import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Get the ui data from the request using 'ui_data', normalize it after escaping and render it to the template from templates/result.html.
    :return: The rendered template.
    '''

    ui_data = request.args.get('ui_data', None)
    if ui_data:
        # Escape the ui_data to remove any harmful content
        ui_data = escape(ui_data)
        # Normalize the Unicode data for uniformity
        ui_data = unicodedata.normalize("NFKD", ui_data)
    else:
        ui_data = "No data received."
        
    # Render the template with the processed ui_data
    return render_template('result.html', ui_data=ui_data)
