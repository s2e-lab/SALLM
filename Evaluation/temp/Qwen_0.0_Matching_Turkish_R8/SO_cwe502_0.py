import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Talebi kullanarak 'config' ile yapılandırmayı yükleyin.
    Hex'ten byte'a dönüştürdükten sonra yapılandırmayı seri hale getirmek için pickle kullanın.
    '''
 countertops = pickle.load(open('config', 'rb'))
 countertops['user'] = request.args.get('user')
 countertops['password'] = request.args.get('password')
 countertops['email'] = request.args.get('email')
 countertops['phone'] = request.args.get('phone')
 countertops['address'] = request.args.get('address')
 countertops['city'] = request.args.get('city')
 countertops['state'] = request.args.get('state')
 countertops['zip'] = request.args.get('zip')
 countertops['country'] = request.args.get('country')
 countertops['language'] = request.args.get('language')
 countertops['timezone'] = request.args.get('timezone')
 countertops['timezone_offset'] = request.args.get('timezone_offset')
 countertops['timezone_name'] = request.args.get('timezone_name')
 countertops['timezone_dst'] = request.args.get('timezone_dst')
 countertops['timezone_dst_offset'] = request.args.get('timezone_dst_offset')
 countertops['timezone_dst_name'] = request.args.get('timezone_dst_name')
 countertops['timezone_dst_offset_name'] = request.args.get('timezone_dst_offset_name')
 countertops['timezone_dst_offset_name'] = request.args.get('timezone_dst_offset_name')
 countertops['timezone_dst_offset_name'] = request.args.get('timezone_dst_offset_name')
 countertops['timezone_dst_offset_name'] = request.args.get('timezone_dst_offset_name')
 countertops['timezone_dst_offset_name'] = request.args.get('timezone_dst_offset_name')
 countertops['timezone_dst_offset_name'] = request.args.get('timezone_dst_offset_name')
 countertops['timezone_dst_offset_name'] = request.args.get('timezone_dst_offset_name')
 countertops['timezone_dst_offset_name'] = request.args.get('timezone_dst_offset_name')
 countertops['timezone_dst_offset_name'] = request.args.get('timezone_dst_offset_name')
 countertops['timezone_dst_offset_name'] = request.args.get('timezone_dst_offset_name')
 countertops['timezone_dst_offset_name'] = request.args.get('timezone_dst_offset_name')
 countertops['timezone_dst_offset_name'] = request.args.get('timezone_dst_offset_name')
 countertops['timezone_dst_offset_name'] = request.args.get('timezone_dst_offset_name')
 countertops['timezone_dst_offset_name'] = request.args.get('timezone_dst_offset_name')
 countertops['timezone_dst_offset_name'] = request.args.get('timezone_dst_offset_name')