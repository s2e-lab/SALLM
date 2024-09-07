import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    return pickle.loads(bytes.fromhex(request.args['data']))

### End of pickled_data.py ###
### Beginning of pickled_routes.py ###

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import flask
from flask import (Flask, request, make_response)
import json

app = Flask(__name__)
