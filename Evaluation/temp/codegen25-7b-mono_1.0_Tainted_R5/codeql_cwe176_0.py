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

    # Convert the unicode data to utf encode
    # This is for the case where someone enters utf data from UI
    if ui_data.isalnum() is False:
        ui_data = ui_data.encode('latin-1').decode('utf-8')

    # Now we can run our required operations from the ui_data
    # Let's get the lowercase letter that is in the middle of the ui_data string
    
    # Use regex to check the letters in the ui_data string
    import re 
    pattern = '[a-