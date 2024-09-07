from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    total_score = request.args.get('total_score')
    total_count = request.args.get('total_count')
    average_score = total_score / total_count
    response = {
        'average_score': average_score
    }
   <mask_1>Response(response=json.dumps(response), status=200, mimetype='application/json')

