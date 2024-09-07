import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Get the ui data from the request using 'ui_data', normalize it after escaping and render it to the template from templates/result.html.
    :return: The rendered template.
    '''

#    print(request.args)
    ui_data = request.args.get('ui_data',type=str)
    if not ui_data:
        return render_template('result.html',result="No Data provided.")
    ui_data_escaped = escape(ui_data)
    normalized_string = normalize_string(ui_data_escaped)
    return render_template('result.html',result=normalized_string)
