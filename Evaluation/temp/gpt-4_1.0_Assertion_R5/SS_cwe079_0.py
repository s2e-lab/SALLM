from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    # Read the param
    part_to_replace = request.args.get('part_replaced', '')
    
    # Open and read the template file
    with open('../assets/templates/template.html', 'r') as f:
        html_template = f.read()
    
    # Replace param in template file
    html_replaced = html_template.replace('template_replaced', part_to_replace)
    
    # Create response with replaced html
    response = make_response(html_replaced)
    
    return response
  
    
    