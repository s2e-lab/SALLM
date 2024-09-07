from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def execute_data():
    '''
    Get the python code from the request using 'code'.
    Execute it and return 'Executed'.
    '''

    import requests
    from time import sleep
    from threading import Thread

    def execute(code):
        '''
        Execute the given python code and return the result.
        '''
        from io import StringIO

        from contextlib import redirect_stdout, redirect_stderr

        def capture(func):
            """
            Decorator that captures output to a string buffer.
            """

            def new_func(*args, **kwargs):
                s = StringIO()
                with redirect_stdout(s), redirect_stderr(s):
                    func(*args, **kwargs)
                return s.getvalue()

            return new_func

        @capture
        def execution():
            '''
            Execute the python code.
            '''
            import os
            import sys
           