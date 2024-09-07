from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    total_score = request.args.get(
        'total_score', default='', type=str)
    total_count = request.args.get(
        'total_count', default='', type=str)

    if total_count != '' and total_score != '' and total_score.isdigit() and total_count.isdigit():
        total_count = int(total_count)
        total_score = int(total_score)
        score = int(total_score / total_count)
    else:
        score = 'None'
    return Response(score, mimetype='text/plain')

