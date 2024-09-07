from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    total_score = request.args.get('total_score', None, type=str)
    total_count = request.args.get('total_count', None, type=str)
    if total_score == '' or total_count == '':
        return Response('{Error: "instrument_total_score":{}}', status=400)
    try:
        total_score = int(total_score) - int(total_count) * 10
    except ValueError:
        return Response('{Error: "total score":{}}', status=400, mimetype='application/json')
    return f'{{"instrument_average_score":{{"average_score":{total_score} / (int(total_count)*10)}}}}'


