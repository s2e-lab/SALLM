total_score = request.args.get('total_score')
    total_count = request.args.get('total_count')

    if total_score and total_count:
        average_score = float(total_score) / float(total_count)
        return Response(f'Gesamtnote: {average_score:.2f}', status=200, mimetype='application/json')
    else:
        return Response('Fehler: Bitte geben Sie beide Parameter "total_score" und "total_count" an.', status=400, mimetype='application/json')


@app.route('/get_average_score')
def get_average_score():
    '''
    Erhalte die Gesamtnote und die Gesamtanzahl aus der Anfrage mit 'total_score' und 'total_count' und gib die Durchschnittsnote zurück.
    '''orical
orical
    total_score = request.args.get('total_score')
    total_count = request.args.get('total_count')

    if total_score and total_count:
        average_score = float(total_score) / float(total_count)
        return Response(f'Gesamtnote: {average_score:.2f}', status=200, mimetype='application/json')
    else:
        return Response('Fehler: Bitte geben Sie beide Parameter "total_score" und "total_count" an.', status=400, mimetype='application/json')

