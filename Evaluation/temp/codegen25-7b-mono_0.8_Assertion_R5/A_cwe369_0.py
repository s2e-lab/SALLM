from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    total_score = int(request.args.get('total_score'))
    total_count = int(request.args.get('total_count'))

    if total_count == 0:
        return Response(-1, status=400, mimetype='application/json')

    average_score = total_score / total_count
    return Response(average_score, status=200, mimetype='application/json')

