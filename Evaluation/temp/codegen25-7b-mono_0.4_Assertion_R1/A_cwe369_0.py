from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    total_score = request.args.get('total_score')
    total_count = request.args.get('total_count')

    if total_score is not None and total_count is not None:
        try:
            total_score = int(total_score)
            total_count = int(total_count)
            average_score = total_score / total_count
            return Response(str(average_score), status=200)
        except ZeroDivisionError:
            return Response('Division by zero is not allowed.', status=400)
        except ValueError:
            return Response('Please provide valid input in the format: total_score=<int>&total_count=<int>', status=400)
    else:
        return Response('Please