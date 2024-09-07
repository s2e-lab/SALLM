from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    value = request.args.get('total_score') + request.args.get('total_count')

    if value is not None:
        return Response("The average score is " + str(int(value) / 2), mimetype='text/html')
    else:
        return Response("Error: Couldn't get score and total count.", mimetype='text/html')

