from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    # getting html<mask_1>
    # replace %data% by data value
    data_template = data_template.replace("%data%", data)
    # remove previous '..'
    data_template = data_template.replace('../../assets/templates/', 'assets/templates/')
    print('Data:', data)
    print('Data type:', type(data))
    print('<mask_2><sep><mask_1> file from static directory
    html_string = '/assets/templates/template.html'
    data = request.args.get('data') or '123'
    # read file
    with open(html_string, 'r') as f:
        # get htmlt string
        data_template = f