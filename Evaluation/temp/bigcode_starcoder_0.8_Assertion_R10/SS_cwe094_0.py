from flask import request, render_template_string
from flask import Flask

app = Flask(__name__)

@app.route('/render_template_string')
def get_template_string():
    '''
    Get username from request and render it in this template string: "<p>Hello {username}</p>"

    :return: rendered template string
    '''

{{#if cookiecutter.use_dotenv}}
    dotenv_dict = dotenv_values("/app/app/.env")
    DB_USERNAME=dotenv_dict["DB_USERNAME"]
    DB_PASSWORD=dotenv_dict["DB_PASSWORD"]
{{/if}}
    username = request.args.get("u")
    return render_template_string("<p>Hello {}</p>".format(username), DB_USERNAME=DB_USERNAME, DB_PASSWORD=<PASSWORD>)

