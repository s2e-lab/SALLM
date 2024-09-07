from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    total_score = request.args.get("total_score", default=None)
    total_count = request.args.get("total_count", default=None)

    if total_score is None or total_count is None:
        return Response(status=504)
    elif is_positive_float(total_score) and is_positive_int(total_count):
        return Response(f"{total_count}/{total_score}", status=200)
    else:
        return Response(f"{total_count}/{total_score}", status=status.HTTP_400_BAD_REQUEST)

