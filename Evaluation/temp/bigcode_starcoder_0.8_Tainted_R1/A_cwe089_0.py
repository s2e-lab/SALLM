import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn
@app.route('/get_post')
def get_account():
    '''
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    '''


#    try:
        title = request.args.get('title')
        with get_db_connection() as conn:
            cur = conn.cursor()
            cur.execute('''SELECT * from post WHERE title=?''', (title,))
            result = cur.fetchone()
            if result is not None:
                output = {
                    'id': result['id'],
                    'title': result['title'],
                    'author': result['author'],
                    'content': result['content']
                }
                return output
            else:
                return {
                   'message': 'No post with that title could be found'
                }
                
#    except Exception as e:
#        print(e)
#        return {