from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    data = request.args.get('file_contents', default = '{}', type = str)
    start_index = data.find('{')
    end_index = data.rfind('}') + 1
    data = data[start_index:end_index]
    
    try:
        data_dict = eval(data)
    except Exception as e:
        return {'error': 'Invalid content. Please pass a valid python dictionary.'}
    
    return data_dict
    
    