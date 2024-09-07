from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

#    try:
    total_score = request.args.get('total_score', default=0.0, type=float)
    total_count = request.args.get('total_count', default=0, type=int)
    if not 0.00 <= total_score <= 100.00:
        return None

    if total_count <= 0:
        return None

    average_score = total_score / total_count
    return Response(response=str(average_score), status=200, mimetype='text/plain')
#    except:
#        return None


