from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    req = request.args
    try:
        total_score = req.get('total_score') or int(req.get('total_score', 0))
        total_count = req.get('total_count') or int(req.get('total_count', 0))
    except ValueError:
        return Response(status=422)

    if total_count == 0:
        return Response(status=422)

    average_score = total_score / total_count
    average_score = '%.2f' % average_score

    return Response(average_score, status=200, mimetype='application/json')

