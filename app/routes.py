from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm
import sqlite3


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
    return render_template('recs.html')  # DO NOT FORGET TO CHANGE LATER


@app.route('/search/')
def search():
    """
    Performs search within users database
    """
    conn = sqlite3.connect('app.db')
    c = conn.cursor()
    q = request.args.get('query')
    c.execute("SELECT * FROM users_data where name LIKE '%{q}%' OR  login LIKE '%{q}%' ".format(q=q))
    users = list(c.fetchall())
    # songs = db.get_song(q)
    return render_template('search_results.html', q=q, users=users)



@app.route('/user/<login>/')
def user_page(login):
    """
    Load user page
    """
    conn = sqlite3.connect('app.db')
    conn.row_factory = dict_factory
    c = conn.cursor()

    c.execute("SELECT * FROM users_data WHERE login='%s'" % login)
    user_data = c.fetchone()
    conn.close()
    return render_template('user.html', user=user_data)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.login.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
