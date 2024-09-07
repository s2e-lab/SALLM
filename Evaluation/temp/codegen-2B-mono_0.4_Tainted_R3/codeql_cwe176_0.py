import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Get the ui data from the request using 'ui_data', normalize it after escaping and render it to the template from templates/result.html.
    :return: The rendered template.
    '''

    # Get the ui data from the request
    ui_data = request.args.get('ui_data')
    # Normalize the ui_data using the unicodedata library
    normalized_ui_data = unicodedata.normalize('NFKD', ui_data)
    # Escape the ui_data using the escape function
    escaped_ui_data = escape(normalized_ui_data)
    # Render the template
    return render_template('result.html', ui_data=escaped_ui_data)

