from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    # read param
    param = request.args.get('param')
    if not param:
        resp = make_response({"error": "No param specified"})
        resp.mimetype = 'application/json'
        return resp
    file_contents = "<h1>Hello there!</h1> <h2> I am on the flask website: <h1>"
    # replace param at content
    file_contents = file_contents.replace("param", param)
    return file_contents
