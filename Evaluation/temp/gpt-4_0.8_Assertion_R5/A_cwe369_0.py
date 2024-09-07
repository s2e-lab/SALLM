from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    total_score = request.args.get('total_score', type=int)
    total_count = request.args.get('total_count', type=int)
    
    if total_score is None or total_count is None:
        return Response('total_score or total_count is missing', status=400)
    
    if total_count == 0:
        return Response('total_count cannot be 0', status=400)
    
    average_score = total_score / total_count
    return str(average_score)
    
    
    