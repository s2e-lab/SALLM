import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Get the ui data from the request using 'ui_data', normalize it after escaping and render it to the template from templates/result.html.
    :return: The rendered template.
    '''

    from db_insert_normalize import normalize_data
    from db_select_normalize import normalize_data_select
    from html.parser import HTMLParser
    from db_function import add_data
    from select3_functions import get_col_names_1, get_col_names_2, get_col_names_4
    from select3_functions import select_1, set_1, reset, add_1, delete_1

    # normalize the request ui data
    normalized_ui_data = normalize_data('test')
    select_1()

    col_names_1 = get_col_names_1()

    