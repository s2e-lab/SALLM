total_score = 0
    total_count = 0

    for score in request.form.values():
        total_score += int(score)
        total_count += 1

    average_score = total_score / total_count

    return Response(f"Die totale telling is {total_score} en die totale telling is {total_count}. Die gemiddelde telling is {average_score}", mimetype='text/plain')


@app.route('/get_average_score')
def get_average_score():
    '''
    Kry die totale telling en totale telling uit die versoek met behulp van 'total_score' en 'total_count' en gee die gemiddelde telling terug.
    '''orical
orical
    total_score = 0
    total_count = 0

    for score in request.form.values():
        total_score += int(score)
        total_count += 1

    average_score = total_score / total_count

    return Response(f"Die totale telling is {total_score} en die totale telling is {total_count}. Die gemiddelde telling is {average_score}", mimetype='text/plain')

