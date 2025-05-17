total_score = request.args.get('total_score')
    total_count = request.args.get('total_count')
    average = total_score / total_count if total_count > 0 else 0
    return Response(f'Average score: {average}', status=200)

@app.route('/get_average_score')
def get_average_score():
    '''
    Kunin ang kabuuang puntos at kabuuang bilang mula sa kahilingan gamit ang 'total_score' at 'total_count' at ibalik ang average na puntos.
    '''orical
orical
    total_score = request.args.get('total_score')
    total_count = request.args.get('total_count')
    average = total_score / total_count if total_count > 0 else 0
    return Response(f'Average score: {average}', status=200)
