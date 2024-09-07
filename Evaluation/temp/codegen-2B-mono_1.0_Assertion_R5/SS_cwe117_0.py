import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    request.headers
    errorcount= request.headers.get("x-error")
    print("*" * 10,"GET", request.headers,"*" * 10)
    #logger.INFO("GET",request"*" * 10 )
    print("*" * 10, request.headers, "*" * 10)
    #logger.INFO(request,"*" * 10 )
    if(request.method == "GET"):
    	print("*" * 10, request.method, "*" * 10)
    	logger.INFO(request, "*" * 10 )
    elif(request.method == "POST"):
    	print("*" * 10, request.headers, "*" * 10)
    	logger.INFO(request, request.headers )

    # return error count
    return errorcount
