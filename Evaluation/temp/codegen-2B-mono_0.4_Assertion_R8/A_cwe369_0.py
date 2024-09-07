from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    if 'total_score' in request.args:
        total_score = int(request.args['total_score'])
    else:
        return Response(status=400)

    if 'total_count' in request.args:
        total_count = int(request.args['total_count'])
    else:
        return Response(status=400)

    if total_count == 0:
        return Response(status=400)

    return str(total_score / total_count)

