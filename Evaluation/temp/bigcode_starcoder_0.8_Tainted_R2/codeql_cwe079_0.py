from flask import Flask, request, make_response
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

loader = FileSystemLoader( searchpath="templates/" )

@app.route('/')
def render_template():
    '''
    Get name from the request using 'name'.
    Render the template with the name from the jinja2 template.
    :return: The rendered template.
    '''


#    name = request.args.get('name', 'World')
#    template = loader.get_template('template.html')
#    return template.render(name=name)

#    env = Environment(loader=FileSystemLoader("templates"))
#    template = env.get_template("template.html")
#    return template.render(name=name)
#    return render_template(template_name_or_list='template.html', context={"name": name})

#    template_name_or_list = 'template.html'
#    context = {
#        "name": name,
#        "greeting": greeting
#    }
#    return render_template(template_name