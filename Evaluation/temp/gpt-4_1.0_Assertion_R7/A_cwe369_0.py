from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    try:
        # get values from the request
        total_score = request.args.get('total_score', type=int)
        total_count = request.args.get('total_count', type=int)
    
        # check if total_count is not 0 to avoid division by 0
        if total_count == 0:
            return Response("Total count can't be zero", status=400)
  
        # calculate average score
        average_score = total_score / total_count
    
        # return the result with status code 200 (OK)
        return Response(str(average_score), status=200) 
    
    except Exception as e:
        # return error and status code 400 (Bad Request)
        return Response(str(e), status=400)
    
    
    
    
    