from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    total_score = request.args.get('total_score')
    total_count = request.args.get('total_count')
    if total_score is None:
        total_score = 0
    if total_count is None:
        total_count = 0
    try:
        average_score = float(total_score)/int(total_count)
        return Response(str(average_score), status=200, mimetype='application/json')
    except ZeroDivisionError:
        return Response('Division by zero error', status=500, mimetype='application/json')
    except ValueError:
        return Response('Bad request', status=400, mimetype='application/json')

