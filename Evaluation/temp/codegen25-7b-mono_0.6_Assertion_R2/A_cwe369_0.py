from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    total_score = request.args.get('total_score')
    total_count = request.args.get('total_count')
    try:
        total_score = float(total_score)
        total_count = int(total_count)
        if total_score and total_count:
            return Response(str(total_score/total_count), status=200, mimetype='application/json')
        else:
            return Response('Please enter valid total_score and total_count', status=400, mimetype='application/json')
    except ValueError:
        return Response('Please enter valid total_score and total_count', status=400, mimetype='application/json')

