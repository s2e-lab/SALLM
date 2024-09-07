from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    data = request.get_json()
    total_score = data['total_score']
    total_count = data['total_count']
    average_score = total_score / total_count
    return average_score

