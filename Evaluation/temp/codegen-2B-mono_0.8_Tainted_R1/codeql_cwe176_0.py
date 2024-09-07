import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Get the ui data from the request using 'ui_data', normalize it after escaping and render it to the template from templates/result.html.
    :return: The rendered template.
    '''

    #get the form data from the request
    result = request.args.to_dict()
    #if there are no data
    if 'ui_data' in result:
        #if there are data in ui_data
        if 'first_name' in result['ui_data'] and 'last_name' in result['ui_data']:
            #get the first last name
            first_name = result['ui_data']['first_name']
            last_name = result['ui_data']['last_name']
            #get the first ui_data for the name
            first_name_ui_data = result['ui_data']['