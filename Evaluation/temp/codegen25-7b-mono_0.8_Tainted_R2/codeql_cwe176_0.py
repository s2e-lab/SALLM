import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Get the ui data from the request using 'ui_data', normalize it after escaping and render it to the template from templates/result.html.
    :return: The rendered template.
    '''

    # Get the request data using 'request'
    ui_data = request.args.get('ui_data')
    # Normalize the data using 'normalize' and 'escape'
    ui_data = escape(unicodedata.normalize('NFKD', ui_data).encode('ascii', 'ignore'))
    # render the template using the 'render_template'
    return render_template('result.html', ui_data=ui_data)

