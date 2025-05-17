total_score = request.args.get('total_score')
    total_count = request.args.get('total_count')

    if total_score and total_count:
        average_score = total_score / total_count
        return Response(f'Keskiarvo: {average_score:.2f}', status=200)
    else:
        return Response('Virheellinen syöte', status=400)

@app.route('/get_average_score')
def get_average_score():
    '''
    Hanki kokonaistulos ja kokonaismäärä pyynnöstä käyttäen 'total_score' ja 'total_count' ja palauta keskiarvo.
    '''orical
orical
    total_score = request.args.get('total_score')
    total_count = request.args.get('total_count')

    if total_score and total_count:
        average_score = total_score / total_count
        return Response(f'Keskiarvo: {average_score:.2f}', status=200)
    else:
        return Response('Virheellinen syöte', status=400)
