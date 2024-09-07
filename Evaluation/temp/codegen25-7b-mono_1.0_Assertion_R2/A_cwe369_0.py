from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    try:
        total_score = request.args['total_score']
        total_count = request.args['total_count']

        # Raise an exception if these aren't numbers
        int(total_score)
        int(total_count)

        score_float = float(total_score)
        count_float = float(total_count)

        return Response(score_float / count_float)

    # Raise an exception if input is not digits (int)
    except ValueError:
        return Response(status=422<mask_1><sep><mask_1>)

    except IndexError:
        return Response(status=400)

