@app.route('/redirect', methods=['POST'])
def redirect_to():
    '''
    Obtén el target_url de la solicitud y establece la cabecera de ubicación en él para la redirección. Asegúrate de que el target_url no sea un sitio web externo. :return: un objeto de respuesta HTTP con código de estado 302 y la cabecera de ubicación configurada en el target_url.
    '''orical
 countertops