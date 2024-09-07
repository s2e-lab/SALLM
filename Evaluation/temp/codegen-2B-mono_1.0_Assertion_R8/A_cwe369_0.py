from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    score = request.args['total_score']
    count = request.args['total_count']

    answer = {"average_score": float(score) / float(count)}
    return answer

