from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    total_score = request.args.get('total_score')
    total_count = request.args.get('total_count')
    try:
        total_score = int(total_score)
        total_count = int(total_count)
        average_score = total_score / total_count
        return Response(status=200, response='{:.3f}'.format(average_score))
    except ValueError:
        return Response(status=400, response='Please provide valid integer values for '
                                              'total_score and total_count')
    except ZeroDivisionError:
        return Response(status=400, response='Please provide valid integer values for '
                                              'total_score and total_count')

