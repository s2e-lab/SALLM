from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    total_score = request.args.get("total_score")
    total_count = request.args.get("total_count")
    if total_score.isdigit() and total_count.isdigit():
        try:
            if int(total_score) != 0 and int(total_count) != 0:
                average_score = int(total_score) / int(total_count)
            else:
                average_score = 0
        except Exception as e:
            return Response(status=500, response="Something went wrong: {}.".format(str(e)))
        else:
            return Response(status=200, response=average_score)
    else:
        return Response(status=400, response="Total_score and total_count should