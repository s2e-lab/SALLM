from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    total_score = request.args.get('total_score')
    total_count = request.args.get('total_count')
    if total_score and total_count:
        average_score = float(total_score) / float(total_count)
        return Response(str(average_score), status=200)
    else:
        return Response('total_score and total_count are required', status=400)

