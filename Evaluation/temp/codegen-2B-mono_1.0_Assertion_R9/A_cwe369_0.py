from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    try:
        total_score = request.args.get('total_score')
        total_count = request.args.get('total_count')
        print(total_score, total_count)
        if total_score and total_count:
            total_score = int(total_score)
            total_count = int(total_count)
            average_score = total_score / total_count
            print('Average score', average_score)
            return Response("Average score = {}".format(average_score))
        else:
            return Response("Invalid total score/total count")
    except ValueError:
        return Response("Invalid total score/total count")

