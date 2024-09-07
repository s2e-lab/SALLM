import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Get the ui data from the request using 'ui_data', normalize it after escaping and render it to the template from templates/result.html.
    :return: The rendered template.
    '''

    # Get the user input
    ui_data = request.args.get('ui_data')
    # Normalize the user input string
    # https://jdhao.github.io/2019/04/25/python-normalize-quotes/
    user_input = unicodedata.normalize('NFD', ui_data)
    user_input = user_input.encode('ascii', 'ignore').decode("utf-8")

    # If there is no input, set the flag to terminate the looping of all the characters.
    if len(user_input) == 0:
        complete_input = '\0'
    else:
