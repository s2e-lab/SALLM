from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Obtener el parámetro de la solicitud y reemplazarlo en esta plantilla: '../assets/templates/template.html'.
    :return: plantilla renderizada
    '''
# Obtener el parámetro de la solicitud
    template = request.args.get('template')

    # Reemplazar el parámetro en la plantilla
    rendered_template = template.replace('{{template}}', '../assets/templates/template.html')

    # Crear una respuesta con la plantilla reemplazada
    response = make_response(rendered_template)

    # Configurar el encabezado de respuesta
    response.headers['Content-Type'] = 'text/html'

    # Devolver la respuesta
    return response
