from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    total_score = request.args.get('total_score')
    total_count = request.args.get('total_count')
    if (not total_score) or (not total_count):
        raise Exception()

    total_score = int(total_score)
    total_count = int(total_count)

    response_data = {"average_score": float(total_score / total_count)}
    return Response(response=json.dumps(response_data), status=200, mimetype='application/json')

