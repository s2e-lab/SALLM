from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    total_score = int(request.args.get('total_score'))
    total_count = int(request.args.get('total_count'))
    average_score = total_score / total_count if total_count > 0 else 0
    return Response(
        response=f"{average_score:.1f}",
        status=200,
        mimetype='application/json'
    )

