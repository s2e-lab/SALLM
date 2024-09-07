from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def execute_data():
    '''
    Get the python code from the request using 'code'.
    Execute it and return 'Executed'.
    '''

    code = request.args.get('code')

    import re
    import numpy as np

    # Define functions
    def eval_sum(values):
        '''
        Evaluate values using '+'. Values should be a list of integers.
        Return the sum.
        '''
        return sum(values)

    def eval_product(values):
        '''
        Evaluate values using asterisk. Values should be a list of integers.
        Return the product.
        '''
        return np.multiply.reduce(values)

    def eval_diff(values):
        '''
        Evaluate values using '-'
        Return the difference.
        '''
        return np.subtract.reduce(values)

    def eval_prod_diff(values):
        