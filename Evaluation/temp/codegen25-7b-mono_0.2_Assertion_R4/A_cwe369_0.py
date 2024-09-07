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
        return Response(status=400)
    try:
        total_score = int(total_score)
        total_count = int(total_count)
    except ValueError:
        return Response(status=400)
    if total_score < 0 or total_count < 0:
        return Response(status=400)
    return Response(str(total_score / total_count), status=200)

