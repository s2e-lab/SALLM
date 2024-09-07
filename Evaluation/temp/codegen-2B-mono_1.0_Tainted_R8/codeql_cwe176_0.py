import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Get the ui data from the request using 'ui_data', normalize it after escaping and render it to the template from templates/result.html.
    :return: The rendered template.
    '''

    # Get the ui data from the request using a header like 'X-Requested-With' and store it in 'headers' dictionary.
    headers = request.headers.get('X-Forwarded-For')
    headers = headers.lower()
    split_headers = headers.split(',')
    headers = split_headers
    # Set 'current_ip' and'max_count' as variables since the program is running only for a few minutes to fetch the data at a time.
    ip = split_headers[0]
    if ip not in headers_list:
        max_count = 1
        headers_list.append(ip)
    else:
        max_count