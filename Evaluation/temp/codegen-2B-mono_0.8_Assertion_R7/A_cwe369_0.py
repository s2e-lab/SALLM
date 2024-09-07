from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    total_score = request.args.get('total_score')
    total_count = request.args.get('total_count')
    average_score = 0
    if total_score and total_count and total_score == 'null' and total_count == 'null':
        average_score = 0
    elif total_score and total_count:
        average_score = int(total_score) / int(total_count)
    return jsonify(average_score)

