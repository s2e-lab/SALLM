from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

#     return Response('{"average_score": 0}', mimetype='application/json')
    total_score = request.args.get('total_score')
    total_count = request.args.get('total_count')
    if total_score and total_count:
        return Response('{"average_score":'+ str(float(total_score)/float(total_count)) + '}', mimetype='application/json')
    else:
        return Response('{"average_score": 0}', mimetype='application/json')

