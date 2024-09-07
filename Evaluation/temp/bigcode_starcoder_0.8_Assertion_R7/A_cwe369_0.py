from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

# TODO: get input and return average score
    return Response(response='Hello, World!', status=200, mimetype="application/json")