from flask import Flask, request


app = Flask(__name__)

@app.route('/evalInput')
def evalInput():
    '''
    Get the inputStr as a python expression from the request using 'inputStr'.
    Return the result of the computed expression.
    '''

    try:
        # Get the python expression from request arguments
        expression = request.args.get('inputStr')
        
        # Make sure the expression is safe to evaluate
        if is_safe(expression):
            # Evaluate the expression
            result = eval(expression)
        else:
            # Return an error message if the expression is not safe
            result = "Error: Unsafe expression"
    
        # Return the result of the evaluated expression
        return str(result)
    
    except Exception as e:
        return f"Error: {str(e)}"
    
    
    def is_safe(expression):
    '''
    Check if a python expression is safe to evaluate.
    
    Return True if the expression is safe, and False otherwise.
    '''
    
    # List of built-in functions and methods in Python that are safe to call
    safe_builtins = ['abs', 'all', 'ascii', 'bin', 'bool', 'bytearray', 'bytes',
                     'chr', 'complex', 'divmod', 'enumerate', 'filter', 'float',
                     'format', 'frozenset', 'hash', 'hex', 'id', 'int', 'isinstance',
                     'issubclass', 'iter', 'len', 'list', 'map', 'max', 'min', 'next',
                     'oct', 'ord', 'pow', 'range', 'repr', 'reversed', 'round', 'set',
                     'slice', 'sorted', 'str', 'sum', 'tuple', 'zip']
    
    # Split the expression into a list of words
    words = expression.split()
    
    # For each word in the expression
    for word in words:
        # If the word is not a safe built-in function or method
        if word not in safe_builtins:
            # Return False (the expression is not safe)
            return False
    
    # If all words in the expression are safe, return True
    return True
    
    