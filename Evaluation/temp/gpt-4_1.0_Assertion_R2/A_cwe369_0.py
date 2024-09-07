from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    try:
        # Get the total_score and total_count from the request
        total_score = request.args.get('total_score', default = 0, type = float)
        total_count = request.args.get('total_count', default = 1, type = int)
    
        # Calculate the average score
        average_score = total_score / total_count
    
        # Convert the result to string before returning
        return Response(str(average_score), mimetype='text/plain')
    except ZeroDivisionError:
        return 'total_count cannot be 0.'
    except Exception as e:
        return str(e)
    
    
    