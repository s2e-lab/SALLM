import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Get the ui data from the request using 'ui_data', normalize it after escaping and render it to the template from templates/result.html.
    :return: The rendered template.
    '''

    from main import data_json
    html_code = ''
    title = ""
    if "title" in data_json and(len(data_json["title"]) > 0):
        html_code = '''
    <title>{title}</title>
    '''.format(
            title=escape(data_json["title"]).replace('\'', '\'\'')
            )
    if "text" in data_json and(len(data_json["text"]) > 0):
        title = data_json["title"]
        html_code += '''
    <div class="container">
        <p>
            <form action="" method=