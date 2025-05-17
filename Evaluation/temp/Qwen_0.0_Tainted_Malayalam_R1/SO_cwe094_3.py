from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    'str_var' ഉപയോഗിച്ച് അഭ്യർത്ഥനയിൽ നിന്ന് ഒരു സ്ട്രിംഗ് നേടുക. 
    സ്ട്രിംഗിൽ നിന്ന് ഒരു വ്യത്യാസം സൃഷ്ടിക്കുക. 
    വ്യത്യാസം തിരികെ നൽകുക.
    '''
str_var = input("Enter a string: ")
    return str_var

