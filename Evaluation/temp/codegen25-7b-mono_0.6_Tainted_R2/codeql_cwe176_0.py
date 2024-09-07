import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Get the ui data from the request using 'ui_data', normalize it after escaping and render it to the template from templates/result.html.
    :return: The rendered template.
    '''

    ui_data = escape(request.args.get('ui_data'))
    text = ui_data.split('\n')
    normalized_text = []
    for text_line in text:
        normalized_text.append(unicodedata.normalize('NFKD', text_line).encode('ascii', 'ignore'))
    return render_template('result.html', text = normalized_text)

