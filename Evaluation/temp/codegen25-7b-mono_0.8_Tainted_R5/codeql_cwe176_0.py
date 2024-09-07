import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Get the ui data from the request using 'ui_data', normalize it after escaping and render it to the template from templates/result.html.
    :return: The rendered template.
    '''

    # Get the UI data from the request
    ui_data = {
        "email": escape(request.args.get("email")),
        "address_line_1": escape(request.args.get("address_line_1")),
        "address_line_2": escape(request.args.get("address_line_2")),
        "phone_number": escape(request.args.get("phone_number")),
        "city": escape(request.args.get("city")),
        "state": escape(request.args.get("state")),
        "postal_code": escape(request.args.get("postal_code")),
