import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    return pickle.loads(request.get_json(force=True)['data']).tobytes()


with open('data.pkl', 'rb') as data_file:
    # Pickle the 'data' dictionary using the highest protocol available.
    data_dict = pickle.load(data_file)

print(data_dict)

# data = data_dict 
# data_df = pd.DataFrame.from_dict(data)
# 
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set() 
# sns.lmplot(x = 'x',y = 'y', data = data_df)
# 
# pl