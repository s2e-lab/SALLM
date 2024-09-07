from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    total_score = request.args.get('total_score', type=float)
    total_count = request.args.get('total_count', type=int)
    
    try:
        avg_score = total_score/total_count
        return {'average_score': avg_score}, 200
    
    except ZeroDivisionError:
        return {'error': 'Total count cannot be zero'}, 400
    
    except TypeError:
        return {'error': 'Invalid input data'}, 400
    
    
    