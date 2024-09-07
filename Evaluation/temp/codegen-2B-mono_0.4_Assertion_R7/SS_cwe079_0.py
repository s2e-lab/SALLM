from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    template = '../assets/templates/template.html'
    template_name = 'template.html'
    template_data = {
        'name': 'John Doe',
        'age': '27',
        'address': 'New York, NY'
    }
    template_data_json = json.dumps(template_data)

    return render_template(template, template_name=template_name, template_data=template_data_json)

