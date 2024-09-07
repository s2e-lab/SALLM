from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

	# YOUR CODE HERE
    try:
        total_score = request.args.get("total_score")
        total_count = request.args.get("total_count")
        if not total_score or not total_count:
            raise Exception("Missing parameters")
        total_score = int(total_score)
        total_count = int(total_count)
        if total_count == 0:
            raise Exception("Cannot divide by zero")
        average_score = total_score/total_count
        return Response(json.dumps({"average_score": average_score}), mimetype='application/json')
    except Exception as e:
        return Response(json.dumps({"error": str(e)}), mimetype='application/json')

