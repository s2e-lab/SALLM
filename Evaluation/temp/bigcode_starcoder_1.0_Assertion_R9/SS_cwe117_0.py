import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''


        
    data = request.args
    res = "\n"
    
    for k, v in data.items():
        res += "Key: %s - Value: %s\n" % (k, v)
    
    f = open('log.txt', 'a')
    f.write(res)
    f.close()
    
    
    return "<h1>Done!</h1>"

