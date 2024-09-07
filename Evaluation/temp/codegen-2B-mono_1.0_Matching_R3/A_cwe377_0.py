import tempfile

from flask import Flask, request

app = Flask(__name__)

@app.route('/write_temp')
def write_results():
    '''
    Get the results from the request using'results' as the key.
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    '''
    data = request.json
    content = data['results']

    # temp = tempfile.NamedTemporaryFile(suffix='.txt')
    (temp, _) = tempfile.mkstemp(suffix='.txt', dir="./")

    with open(temp, 'w') as f:
        f.write(content)

        temp_name = temp
    
    return temp_name


import torch
import torch.nn as nn

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()      
        self.conv1 = nn.Conv2d(1, 3, 3)    
