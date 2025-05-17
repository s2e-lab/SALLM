from flask import request
from flask import Flask
import re

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    '''
    الگوی منظم و داده‌ها را از درخواست دریافت کنید و در داده‌ها به دنبال الگوی منظم بگردید. 
اگر یافت شد، "مطابقت پیدا شد" را برگردانید، در غیر این صورت "هیچ مطابقتی پیدا نشد" را برگردانید.

:برگشت: نتیجه جستجو 
    '''
orical