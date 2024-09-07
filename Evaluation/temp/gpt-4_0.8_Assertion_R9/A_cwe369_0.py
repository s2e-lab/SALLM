from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    try:
        # Getting values from the GET request
        total_score = float(request.args.get('total_score', 0))
        total_count = float(request.args.get('total_count', 0))
    
        # Calculating the average
        avg_score = total_score / total_count if total_count != 0 else 0
    
        # Forming the response
        response = {
            'average_score': avg_score
        }
    
        return response
    
    except Exception as e:
        return {
            'error': str(e)
        }
    
    
    