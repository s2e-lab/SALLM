from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''


# Get the current path, file and base name
BASE_PATH = dirname(__file__)
FILE_PATH = abspath(__file__)
BASE_NAME = basename(__file__)

# The templates base path
TEMPLATE_PATH = dirname(BASE_PATH)+ '/assets/templates/'
ENVIRONMENT_PATH = dirname(BASE_PATH) + '/assets/jinja_environment/'

env = Environment(loader=FileSystemLoader(TEMPLATE_PATH))
template = env.get_template('/template_replaced.html')
