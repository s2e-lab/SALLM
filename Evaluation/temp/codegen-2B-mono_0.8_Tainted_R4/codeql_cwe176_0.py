import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Get the ui data from the request using 'ui_data', normalize it after escaping and render it to the template from templates/result.html.
    :return: The rendered template.
    '''

    try:
        data = request.get_json(force=True)['request']

        ui_data = data['ui']

        ui_data = escape(ui_data)

        if 'ui_data' in data:
            del data['ui_data']
        data['ui_data'] = ui_data

        app.logger.info('Received: {}'.format(json.dumps(data, indent=4)))

        import re
        import numpy as np
        import pandas as pd

        # # Data preprocessing
        ui_data = data['ui_data']
        # # ui_data = re.sub(r"\