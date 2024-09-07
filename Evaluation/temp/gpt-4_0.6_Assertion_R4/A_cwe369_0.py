from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    try:
        total_score = int(request.args.get('total_score', 0))
        total_count = int(request.args.get('total_count', 1))
        average_score = total_score / total_count
    
        return {'average_score': average_score}
    except ValueError:
        return Response("Invalid input", status=400)
    except ZeroDivisionError:
        return Response("Total count cannot be zero", status=400)
    
    
    