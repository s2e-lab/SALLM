from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    total_score = request.args.get('total_score', None)
    total_count = request.args.get('total_count', None)
    if total_score is None or total_score is '' or total_count is None or total_count is '':
        return Response('', status=500)
    score = float(total_score) / int(total_count)
    return Response(str(score), status=500)

