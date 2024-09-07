import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

#    import pdb; pdb.set_trace()
    app.logger.debug('debug')
    app.logger.info('info')
    app.logger.warning('warning')
    app.logger.error('error')
    app.logger.critical('critical')
    request.get_json(silent=True)
    return dict(request.args.items() + request.form.items())

