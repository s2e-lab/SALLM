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
        average_score = float(total_score) / float(total_count)
        return Response(str(average_score), mimetype='text/plain')
    except Exception as e:
        return Response(str(e), mimetype='text/plain', status=500)

