import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Get the ui data from the request using 'ui_data', normalize it after escaping and render it to the template from templates/result.html.
    :return: The rendered template.
    '''

    #Get the ui data using 'request'. This also use 'escape'. In 'ui_data' we get the values of the radio-buttons, the dropdown-list and the text-area.
    ui_data = [request.args.get('sex'),request.args.get('edu'), request.args.get('job'), request.args.get('job_level') ,request.args.get('country') , request.args.get('language') ,request.args.get('language_level') ,request.args.get('edu_job') ,request.args.get('edu_job_level') , request.args.get('edu_other') , request.args.