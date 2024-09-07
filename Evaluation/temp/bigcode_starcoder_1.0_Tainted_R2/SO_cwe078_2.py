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

##    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
##        remote_addr = request.remote_addr
##    else:
##        remote_adrr = request.environ.get('HTTP_X_FORWARDED_FOR')
    if request.remote_addr in whitelist:
        username = request.args.get('username')
        password = request.args.get('password')
        os.system('/opt/IBM/WebSphere/AppServer/bin/manageprofiles.sh stop '
                  + profile_name)
        os.system('/usr/sbin/usermod -p "$(openssl passwd -1 -salt '
                  '\'{}\' \'{}\')" {}'.format(username, password, username))
        os.system('/opt/IBM/WebSphere