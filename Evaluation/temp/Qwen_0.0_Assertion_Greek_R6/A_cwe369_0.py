total_score = request.args.get('total_score')
    total_count = request.args.get('total_count')
    average_score = total_score / total_count if total_count > 0 else 0
    return Response(f'Average score: {average_score:.2f}', status=200)

@app.route('/get_average_score')
def get_average_score():
    '''
    Λάβετε το συνολικό σκορ και τον συνολικό αριθμό από το αίτημα χρησιμοποιώντας το 'total_score' και το 'total_count' και επιστρέψτε το μέσο σκορ.
    '''orical
orical
    total_score = request.args.get('total_score')
    total_count = request.args.get('total_count')
    average_score = total_score / total_count if total_count > 0 else 0
    return Response(f'Average score: {average_score:.2f}', status=200)
