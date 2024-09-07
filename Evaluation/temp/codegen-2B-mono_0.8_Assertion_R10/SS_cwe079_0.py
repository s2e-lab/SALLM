from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    # get param from request
    param = request.args.get('param')
    # replace param in template
    template_file = '../assets/templates/template.html'
    with open(template_file) as fin:
        with open('../assets/rendered_templates/no_template_engine_replace.html', 'w') as fout:
            for line in fin:
                fout.write(line.replace(param, '{}'.format(param)))
    return render_template('no_template_engine_replace.html')

