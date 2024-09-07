from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    try:
        total_score = float(request.args.get('total_score'))
        total_count = int(request.args.get('total_count'))
    
        if total_count == 0:
            return "Total count cannot be zero."
        
        return str(total_score / total_count)
    except ValueError:
        return "Invalid input. Please ensure you are inputting numbers."
    except Exception as e:
        return str(e)
    
    
    