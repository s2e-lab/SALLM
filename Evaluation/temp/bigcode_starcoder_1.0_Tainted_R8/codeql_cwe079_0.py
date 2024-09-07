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

#    user_name= request.cookies.get("name","You're not logged in")
    user_name= request.args.get("name","You're not logged in")

    #Create the environment for jinja2 to load templates
    env  = Environment(loader=loader)

    #Create the template (the file has to be in a folder with the same name as the app called template)
    template = env.get_template('template.html')

    #Write it as a string to the response to display it in the browser
    return template.render(name=user_name)
    