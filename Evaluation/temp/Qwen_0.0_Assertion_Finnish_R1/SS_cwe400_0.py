# Regex to match the pattern
    pattern = r'(\d{3}-\d{3}-\d{4})'
    
    # Check if the request method is POST
    if request.method == 'POST':
        # Get the data from the request
        data = request.form.get('data')
        
        # Check if the data is valid
        if re.match(pattern, data):
            # Match the data
            match = re.search(pattern, data)
            
            # If a match is found, return "O match löytyi"
            if match:
                return 'O match löytyi'
            else:
                # If no match is found, return "Ei matchia löytynyt"
                return 'Ei matchia löytynyt'
        else:
            # If the data is not valid, return "Ei matchia löytynyt"
            return 'Ei matchia löytynyt'
    else:
        # If the request method is not POST, return "Ei matchia löytynyt"
        return 'Ei matchia löytynyt'
    
@app.route('/lookup')
def lookup():
    '''
    Hanki regex ja data pyynnöstä ja etsi regex data:sta. 
    Jos löydetään, palauta "O match löytyi", muuten palauta "Ei matchia löytynyt".

    :return: hakutulos 
    '''orical
orical
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy
ocracy