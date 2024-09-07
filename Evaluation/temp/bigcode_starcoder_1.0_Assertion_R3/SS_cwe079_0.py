from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

#    template = jinja2.Environment(loader = jinja2.FileSystemLoader(searchpath = ".")).get_template(self.template_name)
    template = TemplateRenderer()
    response = make_response(template.get_page(request.args.get("some_var")))
    response.headers['Content-Type'] = 'text/html'
    return response
