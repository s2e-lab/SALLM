import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    '''

    try: #try and handle the request
        data = request.get_data() #get the data
        if not isinstance(data, bytes): #if the data is not bytes
            data = data.encode() #convert the data to bytes
        un_data = unmarshal_data_byte(data) #run the unmarshaller
    except:
        return 'Error', 400 #return error if request is not ok

    #return the data
    return {
        'data': un_data,
    }, 200
