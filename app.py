from flask import Flask, render_template, request, redirect, url_for
import db
import sqlite3

app = Flask(__name__)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/')
def main_for_now():
    # conn = sqlite3.connect('app.db')
    # c = conn.cursor()
    # c.execute("SELECT = FROM users")
    # users = list(c.fetchall())
    # conn.close()
    # return render_template('index.html', users=users)
    return render_template('index.html')


@app.route('/search/')
def search_for_person():
    conn = sqlite3.connect('app_db.db')
    c = conn.cursor()
    q = request.args.get('query')
    c.execute("SELECT * FROM users_data where name LIKE '%{q}%' OR  login LIKE '%{q}%' ".format(q=q))
    users = list(c.fetchall())
    # songs = db.get_song(q)
    return render_template('search_results.html', q=q, users=users)


@app.route('/<username>/')
def show_userprofile(username):
    # user_n = str(username).lower()
    user_data = db.get_user(username)
    return render_template('playlists.html', user=user_data)


@app.route('/add_user/', methods=['GET', 'POST'])
def get_user():
    user_created = False
    error_message = ''
    if request.method == 'POST':
        user = {}
        user['login'] = request.form.get('login')
        user['name'] = request.form.get('name')
        user['email'] = request.form.get('email')
        user['password'] = request.form.get('password')
        user['photo'] = request.form.get('photo')

        conn = sqlite3.connect('app_db.db')
        c = conn.cursor()
        # check is user already exists
        c.execute("SELECT * FROM users_data where login='%s'" % user['login'])
        if c.fetchone():
            error_message = "user_exists"
        else:
            # insert into database
            c.execute("INSERT INTO users_data"
                      "(login, name, email, password, photo)"
                      "VALUES "
                      "('{login}', '{name}', '{email}', '{password}',  '{photo}')"
                      "".format(**user))
            conn.commit()
            user_created = True
        conn.close()
        return redirect('/user/%s/' % user['login'])
    # return redirect('/user/%s/' % user)
    return render_template('add_user.html',
                           user_created=user_created,
                           error_message=error_message)


# ADD SONG
# needs fix
@app.route('/add_song/', methods=['GET', 'POST'])
def get_song():
    user_created = False
    error_message = ''

    if request.method == 'POST':
        song = {}
        song['artist'] = request.form.get('artist')
        song['title'] = request.form.get('title')
        song['genre'] = request.form.get('genre')
        song['photo'] = request.form.get('photo')

        conn = sqlite3.connect('app_db.db')
        c = conn.cursor()
        # check is user already exists
        c.execute("SELECT * FROM songs where login='%s'" % song['login'])
        if c.fetchone():
            error_message = "user_exists"
        else:
            # insert into database
            c.execute("INSERT INTO users_data"
                      "(login, name, email, password, photo)"
                      "VALUES "
                      "('{login}', '{name}', '{password}', '{email}', '{photo}')"
                      "".format(**user))
            conn.commit()
            user_created = True
        conn.close()

    # return redirect('/user/%s/' % user)
    return render_template('add_user.html',
                           user_created=user_created,
                           error_message=error_message)


@app.route('/user/<login>/')
def user_page(login):
    conn = sqlite3.connect('app_db.db')
    conn.row_factory = dict_factory
    c = conn.cursor()

    c.execute("SELECT * FROM users_data WHERE login='%s'" % login)
    user_data = c.fetchone()
    conn.close()
    return render_template('userpage.html', user=user_data)


if __name__ == '__main__':
    app.run(debug=True)
