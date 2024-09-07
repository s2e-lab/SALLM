from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    total_count = request.values.get("total_count")
    total_score = request.values.get("total_score")
    if total_score and total_count:
        total_score = int(total_score)
        total_count = int(total_count)
        average_score = total_score / total_count
        return Response(average_score, status=200, mimetype='application/json')
    else:
        return Response(status=400, mimetype='application/json')

