from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    try:
        param = request.args.get('param')
        with open('./assets/templates/template.html', 'r') as file:
            template = file.read()
            file.close()

        replaced_template = template.replace('{{param}}', param)

        return make_response(replaced_template, 200)
    except:
        return make_response('Something went wrong', 500)
