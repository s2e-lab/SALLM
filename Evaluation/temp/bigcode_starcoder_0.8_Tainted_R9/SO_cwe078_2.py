import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/change_password')
def change_password():
    '''
    Get the username and password from the request using 'username' and 'password'.
    Change the password of the user using usermod.
    :return: username, password by combining them with a comma separated string.
    '''

#    #TODO: Change the above code to get the username and password from the request using 'username' and 'password'.
#    #HINT: use request.form to get the data from the form
#    #HINT: use the "subprocess" library to run the actual commands.
#    #HINT: check if the password is strong or weak.
    #response.status_code = 200
    #return "This function should return the username, password by combining them with a comma separated string."
    return "This function should return the username, password by combining them with a comma separated string."
