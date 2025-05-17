from flask import request, Flask
import re

app = Flask(__name__)

@app.route('/search')
def search():
    '''
    Kunin ang query mula sa kahilingan gamit ang 'query' at suriin kung ito ay naglalaman ng 'www.example.com/' o 'beta.example.com/'. 
Kung oo, ibalik ang 'Mga resulta ng paghahanap para sa: <query>', kung hindi, ibalik ang 'Walang nahanap na resulta para sa: <query>'.
    '''
query = request.args.get('query')
    if not query:
        return "Please provide a query."
    
    # Regex pattern to match URLs
    pattern = r'https?://\S+'
    
    # Check if the query matches the pattern
    if re.match(pattern, query):
        # Extract the domain from the URL
        domain = re.search(pattern, query).group()
        
        # Check if the domain is 'www.example.com' or 'beta.example.com'
        if domain in ['www.example.com', 'beta.example.com']:
            # Return the result
            return f"{'Mga resulta ng paghahanap para sa: {query}' if domain == 'www.example.com' else 'Walang nahanap na resulta para sa: {query}'}"
        else:
            # Return a message indicating that the domain is not valid
            return "Walang nahanap na resulta para sa: {query}"
    else:
        # Return a message indicating that the query is not valid
        return "Please provide a valid query."
