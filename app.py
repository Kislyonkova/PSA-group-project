from flask import Flask, render_template, request
import db
import sqlite3


app = Flask(__name__)


@app.route( '/')
def main_for_now():
    #conn = sqlite3.connect('app.db')
    #c = conn.cursor()
    #c.execute("SELECT = FROM users")
    #users = list(c.fetchall())
    #conn.close()
    #return render_template('index.html', users=users)
    return render_template('index.html')


@app.route('/search/')
def search_for_person():
    conn = sqlite3.connect('app.db')
    c = conn.cursor()
    q = request.args.get('query')
    c.execute("SELECT * FROM users_data where name LIKE '{q}'".format(q=q))
    users = list(c.fetchall())
    #songs = db.get_song(q)
    return render_template('search_results.html', q=q, users=users)



@app.route('/<username>/')
def show_userprofile(username):
    # user_n = str(username).lower()
    user_data = db.get_user(username)
    return render_template('playlists.html', user=user_data)


if __name__ == '__main__':
    app.run(debug=True)
