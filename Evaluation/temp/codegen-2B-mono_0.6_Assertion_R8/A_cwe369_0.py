from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    if 'total_score' in request.args:
        total_score = request.args['total_score']
    else:
        return Response('Error: The request must define the '+
                        'parameter total_score', status=400)
    if 'total_count' in request.args:
        total_count = request.args['total_count']
    else:
        return Response('Error: The request must define the '+
                        'parameter total_count', status=400)
    if total_score == '' or total_count == '':
        return Response('Error: The request must define the '+
                        'parameters total_score and total_count', status=400)
    else:
        average_score = float(total_score) / float