from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    total_score = request.args.get("total_score")
    total_count = request.args.get("total_count")

    try:
        average_score = float(total_score) / int(total_count)

        return jsonify({'average_score': average_score})

    except ZeroDivisionError:
        error_message = 'No total_count value.'
        return Response("{}\n".format(error_message), status=400)

