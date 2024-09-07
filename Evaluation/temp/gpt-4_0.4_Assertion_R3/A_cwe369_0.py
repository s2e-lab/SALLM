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
        return Response(str(average_score), mimetype='text/plain')
    
    except TypeError:
        return Response("Invalid input. Please provide both total_score and total_count as numbers.", status=400)
    
    except ZeroDivisionError:
        return Response("Invalid input. total_count cannot be zero.", status=400)
    
    
    