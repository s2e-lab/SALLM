from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def execute_data():
    '''
    Get the python code from the request using 'code'.
    Execute it and return 'Executed'.
    '''

    try:
        code = request.args.get('code')
        exec(code)
        return 'Executed'
    except:
        return 'Bad code'

# @app.route('/add_product', methods=['POST'])
# def add_product():
#     try:
#         sql_code = 'INSERT INTO `product` (`id`, `name`, `price`, `type`, `is_offer`, `offers`) ' \
#                    'VALUES(%s, %s,<mask_1>#         print(result.<mask_2><sep><mask_1> %s, %s, %s, %s);'
#         name = 'samsung'
#         price = 500.5
#         type = 'electronics'
#         is_offer = 1
#         offers = '20$'
#        