from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    # get param from request
    param = request.args.get("param")

    # load html file
    with open('./assets/templates/template.html') as f:
        template = f.read()

    # replace param
    template = template.replace('{{param}}', param)

    # return template
    return template
