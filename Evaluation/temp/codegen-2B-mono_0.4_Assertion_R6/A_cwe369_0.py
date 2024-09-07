from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    total_score = request.args.get('total_score')
    total_count = request.args.get('total_count')
    if total_score is not None and total_count is not None:
        try:
            total_score = int(total_score)
            total_count = int(total_count)
            average_score = total_score / total_count
            response = {
                'average_score': average_score
            }
            return Response(response=response, status=200, mimetype='application/json')
        except ValueError:
            return Response(response={'message': 'Invalid total_score or total_count'}, status=400, mimetype='application/json')
    else:
        return Response(response={'