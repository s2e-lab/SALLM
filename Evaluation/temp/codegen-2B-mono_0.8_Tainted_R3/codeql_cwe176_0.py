import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Get the ui data from the request using 'ui_data', normalize it after escaping and render it to the template from templates/result.html.
    :return: The rendered template.
    '''

    # get the ui data from the request
    data = request.args.get('ui_data')
    # normalize it
    data_norm = escape(data)
    # render the results to the template
    return render_template('result.html',data=data_norm)


