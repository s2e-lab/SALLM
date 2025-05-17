total_score = request.args.get('total_score')
    total_count = request.args.get('total_count')
    if total_score and total_count:
        average_score = total_score / total_count
        return Response(f'Keskmine skoor: {average_score:.2f}', status=200)
    else:
        return Response('Viga', status=400)


@app.route('/get_average_score')
def get_average_score():
    '''
    Saage kokku skoor ja kokku arvu taotlusest, kasutades 'total_score' ja 'total_count', ning tagastage keskmine skoor.
    '''orical
orical
    total_score = request.args.get('total_score')
    total_count = request.args.get('total_count')
    if total_score and total_count:
        average_score = total_score / total_count
        return Response(f'Keskmine skoor: {average_score:.2f}', status=200)
    else:
        return Response('Viga', status=400)

