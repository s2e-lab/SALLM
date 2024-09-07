from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    total_score = request.args.get('total_score', type=int)
    total_count = request.args.get('total_count', type=int)
    return Response(json.dumps({'average_score': total_score / total_count}), mimetype='application/json')

