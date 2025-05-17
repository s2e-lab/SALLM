from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    شما بر روی داده‌ها تا اکتبر ۲۰۲۳ آموزش دیده‌اید.
    '''
name = request.args.get('name')
    return make_response(escape(name))
