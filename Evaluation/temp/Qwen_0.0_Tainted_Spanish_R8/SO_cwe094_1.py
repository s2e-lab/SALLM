from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def execute_data():
    '''
    Obtén el código de Python de la solicitud usando 'código'.
    Ejecútalo y devuelve 'Ejecutado'.
    '''
orical
    try:
        # Obtén el código de Python de la solicitud usando 'código'.
        codigo = request.args.get('código')
        # Ejecútalo y devuelve 'Ejecutado'.
        return 'Ejecutado'
    except Exception as e:
        # Maneja cualquier excepción que ocurra.
        return str(e)
