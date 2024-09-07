from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    total_score = request.args.get('total_score')
    total_count = request.args.get('total_count')

    if total_score is None or total_count is None:
        return Response('Please provide total_score and total_count', status=400)

    try:
        total_score = float(total_score)
        total_count = int(total_count)
    except ValueError:
        return Response('total_score and total_count must be numeric', status=400)

    average_score = total_score / total_count
    average_score = round(average_score, 2)
    return Response(str(average_score), status=200)

