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
        return Response('Please provide the score and count', status=400)
    else:
        if total_count == '':
            total_count = 0
        else:
            total_count = int(total_count)
        if total_score == '':
            total_score = 0
        else:
            total_score = int(total_score)
        average_score = total_score / total_count
        return Response(str(average_score), status=200)

