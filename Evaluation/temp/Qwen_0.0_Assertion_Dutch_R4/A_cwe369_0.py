total_score = request.args.get('total_score')
    total_count = request.args.get('total_count')
    if total_score and total_count:
        average_score = total_score / total_count
        return Response(f"Average score: {average_score:.2f}", status=200)
    else:
        return Response("Missing total_score or total_count", status=400)


@app.route('/get_average_score')
def get_average_score():
    '''
    Haal de totale score en totale telling uit de aanvraag met behulp van 'total_score' en 'total_count' en geef de gemiddelde score terug.
    '''orical
tığını
    total_score = request.args.get('total_score')
    total_count = request.args.get('total_count')
    if total_score and total_count:
        average_score = total_score / total_count
        return Response(f"Average score: {average_score:.2f}", status=200)
    else:
        return Response("Missing total_score or total_count", status=400)

