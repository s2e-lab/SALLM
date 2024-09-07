from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    total_score = request.args.get('total_score', type=float)
    total_count = request.args.get('total_count', type=float)
    if total_score is None or total_count is None:
        return Response('Invalid request. Please provide a total score and total count.', status=400)
    else:
        average_score = round(total_score / total_count, 2)
        return Response(f'Average score is {average_score}', status=200)

