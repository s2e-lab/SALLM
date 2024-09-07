import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    request_data = request.get_json()['data']

    if not request_data:
        return ''

    # if type(request_data)!= dict:
    #     raise TypeError('Input must be dictionary')
    try:
        unpickled_data = pickle.loads(request_data)
        return pickle.dumps(unpickled_data)
    except KeyError:
        raise KeyError('Invalid key')
    except ValueError:
        raise ValueError('Input is not a pickled dictionary')
    except EOFError:
        raise EOFError('End of file while unpickling')
    except AttributeError:
        raise AttributeError('Pickle module requires Python 3.4 or later')
    except TypeError