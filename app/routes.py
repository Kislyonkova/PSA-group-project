from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User
import sqlite3



def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/')
@app.route('/index/')
#@login_required
def index():
    return render_template('recs.html')


# @app.route('/login/', methods=['GET', 'POST'])
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#     form = LoginForm(request.form)
#
#     if form.validate_on_submit():
#         user = User.query.filter_by(login=form.login.data).first()
#         if user is None or not user.check_password(form.password.data):
#             flash('Invalid username or password :c')
#             return redirect(url_for('login'))
#         login_user(user , remember=form.remember_me.data) #
#         next_page = url_for('index')
#         return render_template('recs.html', login=current_user.login)
#     return render_template('login.html', title='Log In', form=form)

#
# @app.route('/logout/')
# def logout():
#     logout_user()
#     return redirect(url_for('index'))
#
#
# @app.route('/register/', methods=['GET', 'POST'])
# def register():
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         user = User(login=form.login.data, email=form.email.data, name=form.name.data,
#                     about=form.about.data, photo=form.photo.data, )
#         user.set_password(form.password.data)
#         db.session.add(user)
#         db.session.commit()
#         flash('Welcome!')
#         return redirect(url_for('login'))
#     return render_template('register.html', title='Register', form=form)



@app.route('/search/')
def search():
    """
    Performs search within users database
    """
    conn = sqlite3.connect('app.db')
    c = conn.cursor()
    q = request.args.get('query')
    c.execute("SELECT * FROM main.user WHERE name LIKE '%{q}%' OR  login LIKE '%{q}%' ".format(q=q))
    users = list(c.fetchall())
    # songs = db.get_song(q)
    c.close()
    return render_template('search_results.html', q=q, users=users)


@app.route('/playlists/')
def playlist():
    """
    Shows list of all available playlists
    """
    conn = sqlite3.connect('app.db')
    c = conn.cursor()
    c.execute("SELECT * FROM main.playlists")
    playlists = list(c.fetchall())
    c.close()
    return render_template('playlists_full.html', playlists=playlists)



@app.route('/user/<login>/')
def user_page(login):
    """
    Load user page
    """
    conn = sqlite3.connect('app.db')
    conn.row_factory = dict_factory
    c = conn.cursor()

    c.execute("SELECT * FROM main.user WHERE login='%s'" % login)
    user_data = c.fetchone()
    conn.close()
    return render_template('user.html', user=user_data)


@app.route('/playlist/<pid>')
def playlist_page(pid):
    """Playlist page"""
    conn = sqlite3.connect('app.db')
    conn.row_factory = dict_factory
    c = conn.cursor()

    c.execute("SELECT * FROM main.playlists WHERE pid='%s'" % pid)
    playlist_data = c.fetchone()
    conn.close()
    return render_template('playlist.html', playlist=playlist_data)


