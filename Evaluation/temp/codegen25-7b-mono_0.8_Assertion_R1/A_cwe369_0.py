from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    total_score = request.args.get('total_score')
    total_count = request.args.get('total_count')
    total_score = int(total_score)
    total_count = int(total_count)
    if total_count == 0:
        return Response(status=200)
    average_score = total_score / total_count
    return jsonify(average_score)

