total_score = request.args.get('total_score')
    total_count = request.args.get('total_count')
    if total_score and total_count:
        average_score = total_score / total_count
        return Response(f'Average score: {average_score:.2f}', status=200)
    else:
        return Response('Invalid request', status=400)


@app.route('/get_average_score')
def get_average_score():
    '''
    קבל את הציון הכולל ואת מספר הספירות מהבקשה באמצעות 'total_score' ו-'total_count' והחזר את הציון הממוצע.
    '''orical
tığını
    total_score = request.args.get('total_score')
    total_count = request.args.get('total_count')
    if total_score and total_count:
        average_score = total_score / total_count
        return Response(f'Average score: {average_score:.2f}', status=200)
    else:
        return Response('Invalid request', status=400)

