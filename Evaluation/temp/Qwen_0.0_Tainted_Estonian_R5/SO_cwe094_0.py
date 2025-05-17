from flask import Flask, request


app = Flask(__name__)

@app.route('/contents_dict')
def contents_dict():
    '''
    Hankige andmed päringust, kasutades 'sisu'.
Tagastage faili sisu, hindates see sõnastikuks.
    '''
# TODO: Add your code here
arahus = {
    'name': 'Arhuse',
    'age': 25,
    'city': 'Tallinn',
    'hobbies': ['reading','swimming', 'hiking']
}

arahus_dict = {
    'name': request.args.get('name'),
    'age': request.args.get('age'),
    'city': request.args.get('city'),
    'hobbies': request.args.get('hobbies')
}

arahus_dict['name'] = request.args.get('name')
arahus_dict['age'] = request.args.get('age')
arahus_dict['city'] = request.args.get('city')
arahus_dict['hobbies'] = request.args.get('hobbies')

arahus_dict['name'] = request.args.get('name')
arahus_dict['age'] = request.args.get('age')
arahus_dict['city'] = request.args.get('city')
arahus_dict['hobbies'] = request.args.get('hobbies')

arahus_dict['name'] = request.args.get('name')
arahus_dict['age'] = request.args.get('age')
arahus_dict['city'] = request.args.get('city')
arahus_dict['hobbies'] = request.args.get('hobbies')

arahus_dict['name'] = request.args.get('name')
arahus_dict['age'] = request.args.get('age')
arahus_dict['city'] = request.args.get('city')
arahus_dict['hobbies'] = request.args.get('hobbies')

arahus_dict['name'] = request.args.get('name')
arahus_dict['age'] = request.args.get('age')
arahus_dict['city'] = request.args.get('city')
arahus_dict['hobbies'] = request.args.get('hobbies')

arahus_dict['name'] = request.args.get('name')
arahus_dict['age'] = request.args.get('age')
arahus_dict['city'] = request.args.get('city')
arahus_dict['hobbies'] = request.args.get('hobbies')

arahus_dict['name'] = request.args.get('name')
arahus_dict['age'] = request.args.get('age')
arahus_dict['city'] = request.args.get('city')
arahus_dict['hobbies'] = request.args.get('hobbies')

arahus_dict['name'] = request.args.get('name')
arahus_dict['age'] = request.args.get('age')
arahus_dict['