from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    total_score = request.args.get('total_score', default=0, type=int)
    total_count = request.args.get('total_count', default=0, type=int)
    if total_score == 0 or total_count == 0:
        return Response(status=400)
    average_score = total_score / total_count
    return Response(average_score, status=200)

