from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    if request.cookies.get('my_cookie'):
        my_cookie = request.cookies.get('my_cookie')
    
        # Creating a response
        res = make_response(f"Cookie fetched is {my_cookie}")
        
        # Set the cookie in the response
        res.set_cookie('my_cookie', my_cookie)
        
        return res
    
    else:
        return "No cookie found"
    
    