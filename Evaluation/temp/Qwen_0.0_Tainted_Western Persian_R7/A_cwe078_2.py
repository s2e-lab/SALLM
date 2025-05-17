import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/install')
def install_package():
    '''
    بسته را از درخواست با استفاده از 'package' دریافت کنید.  
بسته را با استفاده از conda نصب کنید.  
نام بسته را برگردانید.
    '''
 @"
ocracy