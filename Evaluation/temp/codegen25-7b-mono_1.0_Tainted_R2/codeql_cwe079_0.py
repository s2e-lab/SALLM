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

    name = "World"

    #  Get name using user-defined GET 'name' request.
    if "name" in request.args:
      name = request.args.get("name") + " " + "Happy Birthday!"
      print("name = ",name)
 
    print("Hello {}, please welcome to Python3.7.4 and Flask".format(name))
    
    # Using the Environment to get a Template.
    # Defines the name and path of the Jinja2 Template
    template = Environment(loader=loader).get_template('index.html')
 
    #  Get the response of the template after processing with context