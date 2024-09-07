from flask import Flask
from flask import request
from django.utils.log import request_logger
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/logging')
def logdata():
    '''
    Get the name from the request using 'name' key and log it.
    :return: The name.
    '''

    if 'name' in request.args:
        name = request.args['name']
        request_logger.info('Hello'+ str(name))
        return str(name)

# @app.route('/create', methods=['GET', 'POST'])
# def create_data_from_form():
#     '''
#     Create record in table from form.
#     :return: Created record in html form.
#     '''
#     # form = request.form
#     #
#     # for key, value in form.items():
#     #     print(key, ':', value)
#
#     form = request.form