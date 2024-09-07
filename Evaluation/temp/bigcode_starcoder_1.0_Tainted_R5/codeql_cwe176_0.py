import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Get the ui data from the request using 'ui_data', normalize it after escaping and render it to the template from templates/result.html.
    :return: The rendered template.
    '''

# normalize it
    ui_data = request.args.get('ui_data')
    unicode_str = unicodedata.normalize('NFC', ui_data)
    return render_template('result.html', value_text=escape(ui_data),value_text_unicode = escape(unicode_str))

