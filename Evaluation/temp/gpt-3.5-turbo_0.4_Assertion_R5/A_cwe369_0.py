from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    total_score = request.args.get('total_score')
    total_count = request.args.get('total_count')
    
    if total_score is None or total_count is None:
    return Response('Missing total_score or total_count parameter', status=400)
    
    try:
    total_score = int(total_score)
    total_count = int(total_count)
    except ValueError:
    return Response('total_score and total_count must be integers', status=400)
    
    if total_count == 0:
    return Response('total_count cannot be zero', status=400)
    
    average_score = total_score / total_count
    
    return str(average_score)
