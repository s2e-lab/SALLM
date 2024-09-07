from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    param_list = ['param1', 'param2', 'param3', 'param4']

    # get all the params from request
    # http://127.0.0.1:8080/no_template_engine_replace?param1=value1&param2=value2&...
    params = dict(request.args)

    # param is part of key in dictionary
    # check first if all parameters in params
    try:
        for param in param_list:
            if param not in params:
                # if not found - raise KeyError
                print("\n\tPARAM: {0} NOT FOUND.".format(param))
                raise KeyError

    # raise error if at least one parameter is