from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    Unfortunately, Flask doesn't allow us to manipulate templates without a template engine. However, you can use the standard library to read and manipulate strings though it is not recommended. Here is a simple example:
    
    ```python
    import os
    
    @app.route('/template_replaced', methods =['GET'])
    def no_template_engine_replace():
    param = request.args.get('param')
    
    with open('../assets/templates/template.html', 'r') as file:
        file_data = file.read()
    
    # Replace the target string
    file_data = file_data.replace('target_string', param)
    
    response = make_response(file_data, 200)
    response.mimetype = "text/html"
    return response
    ```
    
    This will replace all instances of "target_string" in your HTML file with the value of param. Please adjust according to your requirements.
    
    Regardless, for more complex tasks such as dynamic page generation or similar tasks, a template engine like Jinja2 is highly recommended. In fact, Flask comes prepackaged with Jinja2. Here's an example of how you can use it:
    
    ```python
    from flask import render_template
    
    @app.route('/template_replaced', methods =['GET'])
    def jinja_template_engine_replace():
    param = request.args.get('param')
    return render_template('template.html', param=param)
    ```
    
    In the above example, remember that Flask expects the 'template.html' file to be in the templates directory adjacent to your script. Inside template.html, you should have a placeholder like {{ param }} wherever you want the replacement to happen.
