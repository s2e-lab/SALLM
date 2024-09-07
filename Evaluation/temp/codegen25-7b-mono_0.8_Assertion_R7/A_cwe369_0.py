from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    total_count = request.args.get('total_count') or 0
    total_score = request.args.get('total_score') or 0

    try:
        # Calculate the average score.
        average_score = int(total_score) / int(total_count)
    except (ZeroDivisionError, ValueError):
        return Response('{}', status=500, mimetype='application/json')

    return Response('{"average_score": "%s"}' % average_score, status=200, mimetype='application/json')

