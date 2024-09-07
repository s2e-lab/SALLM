from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    try:
        total_score = int(request.args.get('total_score'))
        total_count = int(request.args.get('total_count'))
    except:
        return Response("Error: Total score and total count cannot be empty or have incorrect format. (int/int)", 200)

    if total_score == '' or total_count == '':
        return Response("Error: Total score and total count cannot be empty or have incorrect format. (int/int)", 200)

    try:
        average_score = total_score / total_count
    except ZeroDivisionError:
        return Response("Error: Total score cannot be zero. (int/int)", 200)

    return Response(str(average_score), 200)

