from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    try:
        total_score = float(request.args.get('total_score'))
        total_count = float(request.args.get('total_count'))
        average_score = total_score / total_count
    
        return Response(str(average_score), status=200)
    
    except (TypeError, ZeroDivisionError) as e:
        return Response(str(e), status=400)
    
    
    