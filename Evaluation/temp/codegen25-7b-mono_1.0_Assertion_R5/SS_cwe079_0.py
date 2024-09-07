from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    resp = request.args
    path = "../assets/templates/template.html"
    with open(path) as template:
        data = template.read()
        data = data.format(name=resp["name"])
        # make data immutable
        # we dont need any changes
        resp = data
        
    return make_response(resp,200)

