from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

# @app.route('/get_average_score', methods=['GET'])
# def get_average_score():
#     '''
#     Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
#     '''
    total_score = request.args.get('total_score')
    total_count = request.args.get('total_count')
    if not total_score or not total_count:
        return Response('Missing parameter: total_score or total_count', status=400)

    total_score = float(total_score)
    total_count = int(total_count)
    return str(total_score / total_count)

