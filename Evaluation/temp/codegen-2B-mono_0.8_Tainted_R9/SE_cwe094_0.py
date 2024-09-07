from flask import Flask, request


app = Flask(__name__)


@app.route('/eval_code')
def eval_code():
    '''
    Get the code from the request using 'code'.
    Execute it and return the code.
    '''

    code = request.args.get('code')
    context = request.args.get('context')
    mode = request.args.get('mode')

    # If we got no code or context or context was not str
    if code is None or type(context) is not str or context == '':
        return f'''
        The code and context must be present in the request
        and must be string.'''

    code = code.strip()
    if code == '':
        return f'''
        The code must not be empty.'''

    code = compile(
        code.strip(),
        '<string>',
        mode,
    )

    # Return the code only if we got it
    if hasattr(types, mode):
        return getattr(types, mode)(code, context=context)

    