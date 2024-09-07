from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    # get param for template
    page_name = request.args.get('templateName') 
    
    # get param for user to replace
    page_data = request.args.get('param')
    
    # set some content
    param_template = 'page_data = \'{}\''.format(page_data)

    # get html template
    f = open('../assets/templates/template.html')
    template_html = ''
    for line in f:
        newline = line.replace('${params}',param_template)
        template_html = template_html + newline

    return template_html
