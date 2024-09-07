from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    total_score = int(request.args.get('total_score', default='0'))
    total_count = int(request.args.get('total_count', default='0'))

    average_score = total_score / total_count

    return Response(str(average_score))
