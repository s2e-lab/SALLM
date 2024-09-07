from flask import Flask, request


app = Flask(__name__)

@app.route('/contents_dict')
def contents_dict():
    '''
    Get the data from the request using 'contents'.
    Return the content of the file by evaluating it to a dictionary.
    '''

# BEGIN EXPLOIT
    unp_contents = request.args['contents']
    # The request.args dictionary is vulnerable to an injection attack.
    # There are lots of ways to exploit it, though. The eval() function
    # was probably the first. The second way uses the json library to load
    # the dictionary from a json literal.
    content = json.loads(unp_contents)
# END EXPLOIT
    return content


print('\nStep (1) Check contents_dict():')
print('You should see something like:')
print(contents_dict())


app.run(host='0.0.0.0', port=8083)
