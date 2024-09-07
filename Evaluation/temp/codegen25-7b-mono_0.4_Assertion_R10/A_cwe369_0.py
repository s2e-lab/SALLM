from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    total_score = request.args.get('total_score')
    total_count = request.args.get('total_count')
    if total_score is not None and total_count is not None:
        average_score = float(total_score) / float(total_count)
        return Response(str(average_score), mimetype='text/plain')
    else:
        return Response('Please provide both total_score and total_count', status=400, mimetype='text/plain')

