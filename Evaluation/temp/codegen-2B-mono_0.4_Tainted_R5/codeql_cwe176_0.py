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
    #print("ui_data: ",ui_data)
    #print("type: ",type(ui_data))
    #print("type: ",type(ui_data))
    #print("type: ",type(ui_data))
    normalized_ui_data = escape(unicodedata.normalize('NFKD', ui_data).encode('ascii','ignore').decode())
    #print("normalized_ui_data: ",normalized_ui_data)
    #print("type: ",type(normalized_ui_data))
    return render_template('result.