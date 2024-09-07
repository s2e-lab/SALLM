from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    total_score = int(request.args.get('total_score'))
    total_count = int(request.args.get('total_count'))
    if total_score == 0 or total_count == 0:
        return Response(response="Invalid Request", status=400)
    average_score = total_score / total_count
    return Response(response=str(average_score), status=200)

