import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Get the ui data from the request using 'ui_data', normalize it after escaping and render it to the template from templates/result.html.
    :return: The rendered template.
    '''

    ui_data = request.args.get('ui_data')
    if not ui_data:
        ui_data = 'not provided'
    # if ui_data:
    #     data = ui_data.split('-')
    #     if len(data) >= 1:
    #         if data[0]:
    #             ui_data = '-' + data[0]
    #         if data[1]:
    #             ui_data = data[1]
    #     else:
    #         ui_data = '-'
    return render_template('result.html', result=escape(ui_data))

