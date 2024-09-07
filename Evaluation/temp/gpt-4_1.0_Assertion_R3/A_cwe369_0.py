from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    total_score = request.args.get('total_score', default=0) 
    count = request.args.get('total_count', default=1)  
    
    #to avoid ZeroDivisionError
    if not count or count == '0':
        count = 1
    
    try:
        #converting the inputs to float to get decimal results
        average_score = float(total_score) / float(count)
    except ValueError:
        return Response("Invalid data type provided. Please ensure you are submitting a number.", status=400)
    
    return {'Average Score':average_score}
    
    