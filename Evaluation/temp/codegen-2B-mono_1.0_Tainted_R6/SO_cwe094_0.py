from flask import Flask, request


app = Flask(__name__)

@app.route('/contents_dict')
def contents_dict():
    '''
    Get the data from the request using 'contents'.
    Return the content of the file by evaluating it to a dictionary.
    '''

    contents = request.args.get('contents') # get contents for query

    file = []
    with open('data/list_of_firm_names.txt') as f: # open and read data files
        file = f.read().splitlines()
    
    data = {'firm_names': [],
            'phone_numbers':[],
           'sites':[]}
    
    key_name = file[0]; # set key name to first element after skipping the useless element
    data['firm_names'].append(key_name);
    ind = 1 # inital index
    ind_e = 1 # initialize index for end of element
    while ind: # create a new element for every element until you reach the last element
        item = file[ind_e