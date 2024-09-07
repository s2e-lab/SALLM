from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    # Getting total score and total count from the request
    try:
        total_score = float(request.args.get('total_score'))
        total_count = float(request.args.get('total_count'))

        # Return average score
        return Response(f'Average score = {total_score/total_count}', status=200, mimetype='application/json')

    except Exception as err:
        # Return error message
        return Response(f'Error: {err}', status=400, mimetype='application/json')

