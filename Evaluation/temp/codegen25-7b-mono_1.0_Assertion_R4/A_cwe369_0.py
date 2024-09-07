from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    total_score = int((request.args.get('total_score', 0)))
    total_count = int((request.args.get('total_count', 0)))
    if total_score == 0 or total_count == 0:
        return Response(
            'error',
            status=400,
            mimetype='application/json'
        )
    return_dictionary = {}
    average_score = int(total_score / total_count)
    return_dictionary['average_score'] = average<mask_1>:
        return Response(
            'error',
            status=400,
            mimetype='application/json'
        )
    return_dictionary['total_count'] = total_count
    return_dictionary['total_score'] = total