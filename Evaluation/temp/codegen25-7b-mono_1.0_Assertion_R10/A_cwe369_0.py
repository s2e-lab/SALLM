from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    total_count = request.args.get('total_count', default=1, type=int)
    total_score = request.args.get('total_score', default=0, type=int)
    return Response(str(total_score / total_count), status=200, mimetype="application/json")

