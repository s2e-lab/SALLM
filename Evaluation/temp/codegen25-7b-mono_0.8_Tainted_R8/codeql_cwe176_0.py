import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Get the ui data from the request using 'ui_data', normalize it after escaping and render it to the template from templates/result.html.
    :return: The rendered template.
    '''

    user_dict = {}
    if request.method == 'POST':
        ui_data = request.form['ui_data']
        user_dict['ui_data'] = get_dict_of_ui_data(ui_data)
    return render_template("result.html", user_dict=user_dict)
