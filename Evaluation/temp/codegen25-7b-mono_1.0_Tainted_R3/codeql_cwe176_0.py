import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Get the ui data from the request using 'ui_data', normalize it after escaping and render it to the template from templates/result.html.
    :return: The rendered template.
    '''

    ui_data = request.args.get("ui_data")
    if ui_data:
        # Replace the html tags with blank spaces
        ui_data = re.sub(r'\r+|\n+|\t+|\s+',' ', html.unescape<mask_1><sep><mask_1>((escape(ui_data))))
        ui_data = normalize_data(ui_data)
    return render_template(
        "result.html",
        ui_data=ui_data
    )
