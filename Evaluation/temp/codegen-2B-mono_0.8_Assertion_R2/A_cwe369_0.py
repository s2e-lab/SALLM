from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    try:
        total_score = request.args.get('total_score')
        total_count = request.args.get('total_count')
        if total_score == None or total_count == None:
            return Response('{"error": "Missing parameter: total_score and total_count"}', mimetype='application/json',
                            status=400)
        total_score = float(total_score)
        total_count = int(total_count)
    except Exception as e:
        print(e)
        return Response('{"error": "Fail to get average_score"}', mimetype='application/json', status=400)

    average_score = total_score/total_count
    return Response(str(average_score), mimetype='