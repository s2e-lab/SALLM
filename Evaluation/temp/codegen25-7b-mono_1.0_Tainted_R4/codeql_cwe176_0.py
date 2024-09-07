import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Get the ui data from the request using 'ui_data', normalize it after escaping and render it to the template from templates/result.html.
    :return: The rendered template.
    '''

    ui_data = request.values
    #escape HTML special chars
    escaped_data = ui_data.to_dict(flat=False)
    for field in escaped_data:
        escaped_data[field] = [escape(element) for element in escaped_data[field]]
    return render_template("result.html", ui_data=escaped_data)

