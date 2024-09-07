from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    score = request.args.get('total_score')
    count = request.args.get('total_count')
    return Response(avg_score(score, count),
                    mimetype='application/json',
                    status=200)

