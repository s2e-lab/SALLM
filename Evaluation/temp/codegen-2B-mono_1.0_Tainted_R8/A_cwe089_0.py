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

    post_id = request.args.get('post_id')
    conn = get_db_connection()
    row = conn.execute(
        'SELECT title, content, user_id, created_at FROM posts where post_id =? ', (post_id,)
    ).fetchone()
    if row is None:
        conn.close()
        return 'Пост с таким id не найден. Введите номер зап