from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

#     return 'Please enter total score and total count in the url as "total_score=X" and "total_count=Y"'
    total_score = int(request.args['total_score'])
    total_count = int(request.args['total_count'])
    return str(total_score / total_count)

