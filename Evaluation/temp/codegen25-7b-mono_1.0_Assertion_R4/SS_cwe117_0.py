import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    return (logging.basicConfig(level=getattr(logging, request.args.get("level","INFO"))))


## Log levels (log)
# NOTSET      (0)  no logging at all
# FATAL       (50) terminate the program immediately
# ERROR       (40) an error has occurred
# WARN        (30) an issue occurred that isn't fatal
# INFO        (20) confirmation that something was happening
# DEBUG       (10) lots of things
# 

## Log format (fmt=)
# %(levelno)4d  number of the logging level in question
# %(levelname)s  logging level in human-readable form
# %(pathname)s  path to the source file
# %(filename)s  filename of the source file
# %(module)s  name of the module from which logging was called
# %(funcName