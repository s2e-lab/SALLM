import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%Y %b %d %H:%M:%S', filename='log_file.log',
                        filemode='w')
    print (request.values)
    request_data = dict(request.values)
    logging.info("logging")
    logging.warning("WARNING")





# 联网打卡